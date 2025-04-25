from PIL import Image
import numpy as np
import math as m
import scipy.signal
import os

def transform_curved_to_flat(image_path):
    image = Image.open(image_path).convert("L")
    gray_array = np.array(image)

    row = [i for i in range(gray_array.shape[0]) if gray_array[i][2] > 10]
    column = [i for i in range(gray_array.shape[1]) if gray_array[2][i] > 10]
    row_cm = (row[-1] - row[1]) / (len(row) - 2)
    column_cm = (column[-1] - column[1]) / (len(column) - 2)
    height = row_cm
    width = column_cm

    gray_row_sums = np.sum(gray_array, axis=1)
    gray_row_id = np.where(gray_row_sums < 1500)[0][0]

    temp = gray_array[gray_row_id:, 6:].copy().astype(float)
    temp[temp > 200] = 0
    temp[temp < 5] = 0
    temp[:100, :100] = 0
    temp[:100, -200:] = 0

    row_sums = np.sum(temp, axis=1)
    row_id = np.where(row_sums > 200)[0][0]
    column_ids = scipy.signal.find_peaks(temp[row_id, :], distance=100)[0]
    cln = column_ids[:2]
    d = abs(cln[0] - cln[1]) / 2
    d_cm = d / width
    theta = 84 / 180 * m.pi
    alpha_image = theta / 2
    ratio = height / width
    alpha_real = m.atan(m.tan(alpha_image) * ratio)
    offset_cm = d_cm / m.sin(alpha_real)
    offset = offset_cm * height
    middle_column = m.floor(cln[0] + d)

    middle_mask = np.where(temp[:, middle_column] > 0)
    first = middle_mask[0][0]
    last = middle_mask[0][-1]
    r = last - first
    r_cm = r / height

    r_mm = r_cm * 10
    offset_mm = offset_cm * 10
    alpha_deg = alpha_real * 180 / m.pi
    alpha = round(alpha_deg)

    rows = np.arange(m.floor(offset_mm), m.floor(offset_mm + r_mm))
    cols = np.arange(-alpha, alpha)
    Th_d, R = np.meshgrid(cols, rows)
    Th = Th_d / 180 * m.pi

    Y = np.cos(Th) * R
    X = np.sin(Th) * R

    x_pixel = X / 10 * width + temp.shape[1] / 2
    y_pixel = Y / 10 * height - (offset - first)

    return trilinear_interpolation(x_pixel, y_pixel, temp)

def trilinear_interpolation(X, Y, temp):
    X_left = np.floor(X).astype(int)
    X_right = np.ceil(X).astype(int)
    Y_top = np.floor(Y).astype(int)
    Y_bottom = np.ceil(Y).astype(int)

    Intensity = np.zeros(X.shape)
    for i in range(Intensity.shape[0]):
        for j in range(Intensity.shape[1]):
            x = X[i, j]
            y = Y[i, j]
            xl, xr = X_left[i, j], X_right[i, j]
            yt, yb = Y_top[i, j], Y_bottom[i, j]
            A = temp[yt, xl]
            B = temp[yb, xl]
            C = temp[yt, xr]
            D = temp[yb, xr]
            Intensity[i, j] = (((x-xl)*C)+(xr-x)*A)/(xr-xl)*(yb-y)/(yb-yt) +                               (((x-xl)*D)+(xr-x)*B)/(xr-xl)*(y-yt)/(yb-yt)
    Intensity = np.clip(Intensity, 0, 255)
    return Intensity
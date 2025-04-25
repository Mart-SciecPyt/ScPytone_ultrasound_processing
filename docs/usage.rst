Introduction: 
ultrasound_processing_package is a Python toolbox designed for the purpose of preprocessing and transformation of ultrasound images. It provides three core capabilities: Convert curved ultrasound scans into flat images, Filtering the contour of a selected object by intensity thresholding, Convert back to curved ultrasound scans. The transformations are essential for the thresholding so we can search for peaks using cartesian coordinates instead of polar coordinates. These modules will be the fundamentals of point cloud generation based on ultrasound images.




Description: 


Loading in: 
Preprocessing and transforming images:
In this module we preprocess the images and transform them to a format which can be used later. We calculate the real-world dimensions of the image and 


Filtering of the ultrasound images: 
In this module, we first generate a binary mask by thresholding the input image: pixels with intensity at or above the specified threshold are set to white (255), and those below are set to black (0). After removing noise components, we scan each column to select the very first pixel whose intensity exceeds the threshold, building an initial contour mask. Next, we apply OpenCV’s functions to thicken that contour for clear visualization. Finally, we apply the dilated contour as a mask to preserve and display the original pixel intensities. 







Usage:
Installation: 
Clone the git repository, or download the code
Navigate to the directory and install with pip
pip install ultrasound_processing_package
Example:


Function
Description
convert_to_grayscale(image)
Converts a color image to grayscale (shades of gray) using the PIL library. Returns the image as a NumPy array.
detect_cm_marks(gray_array)
Detects small calibration marks (e.g., ruler ticks) on the top and left edges of the image to estimate scale (d in pixels per cm). Returns scale, row marks, and column marks.
clean_image(gray_array)
Cleans the grayscale image by cropping and removing background noise (intensity too bright or too dark). Returns the cleaned image and the row index where useful data starts.
calculate_geometry(temp,d, alpha)
Calculates physical geometry like offset (horizontal distance), range (vertical extent), and their cm/pixel conversions. Uses peak detection and trigonometry (alpha is an angle in radians).
compute_coordinate_grid(offset_cm, r_cm, d, temp, offset_px, first, alpha_deg, res)
Builds a coordinate grid for the image using polar coordinates (radius & angle). Converts to Cartesian grid (X, Y in image) for interpolation.
trilinear_interpolation(X, Y, temp)
Estimates pixel intensity values at non-integer (subpixel) coordinates using bilinear interpolation (a type of weighted average).
transform(path, alpha_deg, res)
The main function: processes an image file end-to-end. Converts to grayscale, detects calibration marks, cleans the image, computes geometry, builds grid, interpolates, and returns a transformed image (intensity) and depth.




EGYÉB TEENDŐK:
transzformáció modult/függvényt átírni hogy ne egy path-ot kelljen megadni, hanem egy grayscale image-t
egységes képet adni a kódoknak: kommentek, kitisztítani a kikommentelt kódrészleteket stb.
Ágó modulját jobban függvényekbe pakolni hogy hasonlítson a többihez ilyen tekintetben is.

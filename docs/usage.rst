Ultrasound Processing Package
=============================

**ultrasound_processing_package** is a Python toolbox designed for preprocessing and transforming ultrasound images.  
It includes three core functionalities:

- Convert curved ultrasound scans into flat images.
- Filter the contour of a selected object by intensity thresholding.
- Convert flat images back into curved ultrasound scans.

These transformations enable precise analysis in Cartesian coordinates instead of polar geometry.  
They form the foundation for point cloud generation from ultrasound data.


Description
===========

1. Preprocessing and Transforming Images
----------------------------------------

In this module, we preprocess the image and convert it into a “flat” format, which is easier to work with during filtering.

- Convert the input image to grayscale.
- Detect and interpret calibration marks along both axes.
- Clean the image by removing irrelevant regions and suppressing extreme pixel values.
- Estimate geometric parameters (e.g., scan area, offset, scanning depth) based on peak detection.
- Use trigonometric relations to build a polar-to-Cartesian coordinate grid.
- Use trilinear interpolation to project the image onto a uniform Cartesian plane.


2. Filtering of the Ultrasound Images
-------------------------------------

In this module, we filter the image using thresholding:

- Pixels with intensity above a threshold are set to white (255), others to black (0).
- Noise is removed using morphological operations.
- For each column, we keep the first pixel exceeding the threshold to define a contour.
- The contour is dilated using OpenCV functions for clarity.
- A mask is created using the dilated contour and applied to the original image to preserve useful intensity data.


3. Backtransformation
---------------------

This module reverses the transformation process:

- Converts Cartesian space data back to polar geometry.
- Defines key transformation parameters and builds a polar grid.
- Excludes regions outside the field of view.
- Finds nearest matching coordinates from the original data.
- Uses trilinear interpolation to fill in the backprojected image based on original data and weights.


Usage
=====

1. Installation
---------------

To install:

.. code-block:: bash

   git clone <repository-url>
   cd ultrasound_processing_package
   pip install ultrasound_processing_package

Make sure to set the proper paths to the files.

2. Example
----------

Martín could you please write a working example for the package here?

*Hyperlinked notebook:*  
`Notebook link <https://colab.research.google.com/drive/1X5UvAwVgtOkaNmMB3ywh5hn7X8JztSir?usp=sharing>`_


Transform Project Module
========================

This module transforms a grayscale ultrasound image from polar-like geometry into a clean Cartesian projection using calibration marks and interpolation.

Steps
=====

#. **Convert to grayscale**  
#. **Detect calibration marks**  
#. **Clean irrelevant parts of the image**  
#. **Calculate geometric parameters**  
#. **Build a Cartesian coordinate grid**  
#. **Interpolate pixel values using the coordinate grid**

Functions
---------

.. autofunction:: convert_to_grayscale
.. autofunction:: detect_cm_marks
.. autofunction:: clean_image
.. autofunction:: calculate_geometry
.. autofunction:: compute_coordinate_grid
.. autofunction:: trilinear_interpolation
.. autofunction:: transform


Function Descriptions
---------------------

convert_to_grayscale(image)
---------------------------

Converts a color image to grayscale using the PIL library.

Parameters
^^^^^^^^^^

:``image``: ``PIL.Image``  

Returns
^^^^^^^

:``grayscale_image``: ``ndarray``  


detect_cm_marks(gray_array)
---------------------------

Detects calibration marks (e.g. ruler ticks) on the image edges and calculates the scale.

Parameters
^^^^^^^^^^

:``gray_array``: ``ndarray``  

Returns
^^^^^^^

:``d``: ``float`` (pixels/cm)  
:``rows``: ``list[int]`` — vertical tick positions  
:``cols``: ``list[int]`` — horizontal tick positions  


clean_image(gray_array)
-----------------------

Removes unnecessary parts and background noise from the grayscale image.

Parameters
^^^^^^^^^^

:``gray_array``: ``ndarray``  

Returns
^^^^^^^

:``temp``: ``ndarray`` — cleaned image  
:``idx``: ``int`` — starting row index of relevant content  


calculate_geometry(temp, d, alpha)
----------------------------------

Calculates physical and pixel-based dimensions from calibration and image structure.

Parameters
^^^^^^^^^^

:``temp``: ``ndarray``  
:``d``: ``float`` — pixels per cm  
:``alpha``: ``float`` — angle in radians  

Returns
^^^^^^^

:``offset_px``: ``float``  
:``r_px``: ``int``  
:``offset_cm``: ``float``  
:``r_cm``: ``float``  
:``first``: ``int`` — top row index of target area  


compute_coordinate_grid(offset_cm, r_cm, d, temp, offset_px, first, alpha_deg, res)
-----------------------------------------------------------------------------------

Builds a 2D polar-to-Cartesian coordinate grid for interpolation.

Parameters
^^^^^^^^^^

:``offset_cm``: ``float``  
:``r_cm``: ``float``  
:``d``: ``float``  
:``temp``: ``ndarray``  
:``offset_px``: ``float``  
:``first``: ``int``  
:``alpha_deg``: ``float``  
:``res``: ``float``  

Returns
^^^^^^^

:``X``: ``ndarray``  
:``Y``: ``ndarray``  


trilinear_interpolation(X, Y, temp)
-----------------------------------

Interpolates grayscale intensity values on a transformed coordinate grid.

Parameters
^^^^^^^^^^

:``X``: ``ndarray`` — X coordinates  
:``Y``: ``ndarray`` — Y coordinates  
:``temp``: ``ndarray`` — cleaned image  

Returns
^^^^^^^

:``intensity``: ``ndarray`` — interpolated image  


transform(path, alpha_deg, res)
-------------------------------

Main transformation pipeline: loads image, detects scale, cleans image, transforms coordinates, and interpolates.

Parameters
^^^^^^^^^^

:``path``: ``str``  
:``alpha_deg``: ``float`` — field-of-view angle in degrees  
:``res``: ``float`` — resolution in pixels/cm  

Returns
^^^^^^^

:``intensity``: ``ndarray``  
:``depth``: ``float``  
:``offset_cm``: ``float``  




Masking Module
==============

This module detects the contour of the desired object within ultrasound images—in our case ships—and cleans point cloud data.

Steps
=====

#. **Setting the threshold**  
#. **Removing noise**  
#. **Selecting first bright pixel exceeding the threshold in each column**  
#. **Contour Dilation**  

Functions
---------

.. autofunction:: mask

mask(image, top_percent=0.93, top_margin=5, apply_closing=True)
----------------------------------------------------------------

Parameters
^^^^^^^^^^

:``image``: ``ndarray``  
:``top_percent``: ``float``, default=0.93  
:``top_margin``: ``int``, default=5  
:``apply_closing``: ``bool``, default=True  

Returns
^^^^^^^

:``masked_image``: ``ndarray``  




Transform Back Project Module
=============================

This module transforms polar ultrasound-like images into Cartesian form using geometric mapping and interpolation techniques.

Steps
=====

#. **Load grayscale data**
#. **Convert between polar and Cartesian coordinates**
#. **Build a grid over the Cartesian space**
#. **Filter valid regions**
#. **Interpolate pixel intensities**

Functions and Classes
---------------------

.. autofunction:: read_png
.. autofunction:: read_png_colored
.. autoclass:: VolumeTransformer
	:members:
.. autofunction:: interp
.. autofunction:: interp_img


Function Descriptions
---------------------

read_png(path)
--------------

Reads a PNG image using matplotlib.

Parameters
^^^^^^^^^^

:``path``: ``str`` — File path to PNG image  

Returns
^^^^^^^

:``image``: ``ndarray``  


read_png_colored(path)
----------------------

Reads and converts a PNG image to grayscale using weighted RGB channels.

Parameters
^^^^^^^^^^

:``path``: ``str`` — File path to PNG image  

Returns
^^^^^^^

:``image_gray``: ``ndarray``  


VolumeTransformer
-----------------

A class to manage coordinate transformations and interpolation.

**__init__(frame_width, frame_depth, depth, thetas, offset, resolution, straighten_volume=False)**

Parameters
^^^^^^^^^^

:``frame_width``: ``int`` — Width of input image in pixels  
:``frame_depth``: ``int`` — Height of input image in pixels  
:``depth``: ``float`` — Physical scan depth  
:``thetas``: ``tuple[float, float]`` — Angular range in radians  
:``offset``: ``float`` — Vertical offset from origin  
:``resolution``: ``float`` — Physical resolution (units/pixel)  
:``straighten_volume``: ``bool`` — Whether to center the angular range (default: False)  


transform_spherical_to_cartesian(R, THETA)
------------------------------------------

Converts polar coordinates to Cartesian space.

Parameters
^^^^^^^^^^

:``R``: ``ndarray``  
:``THETA``: ``ndarray``  

Returns
^^^^^^^

:``X``: ``ndarray``  
:``Z``: ``ndarray``  


transform_cartesian_to_spherical(X, Z)
--------------------------------------

Converts Cartesian coordinates to polar.

Parameters
^^^^^^^^^^

:``X``: ``ndarray``  
:``Z``: ``ndarray``  

Returns
^^^^^^^

:``R``: ``ndarray``  
:``THETA``: ``ndarray``  


create_image_volume()
---------------------

Creates coordinate grids and masks invalid regions based on geometry.

Parameters
^^^^^^^^^^

None  

Returns
^^^^^^^

None  


find_nearest()
--------------

Computes neighboring indices and weights for interpolation.

Parameters
^^^^^^^^^^

None  

Returns
^^^^^^^

None  


trilinear_interpolation(frame)
------------------------------

Performs interpolation using surrounding data points.

Parameters
^^^^^^^^^^

:``frame``: ``ndarray`` — Input 2D image  

Returns
^^^^^^^

:``interpolated_frame``: ``ndarray``  


interp_img(frame, depth, alpha, offset_frame, offset=0, resolution=0.01)
------------------------------------------------------------------------

Main function to interpolate an image.

Parameters
^^^^^^^^^^

:``frame``: ``ndarray``  
:``depth``: ``float``  
:``alpha``: ``float``  
:``offset_frame``: ``float``  
:``offset``: ``float``, default=0  
:``resolution``: ``float``, default=0.01  

Returns
^^^^^^^

:``interpolated_image``: ``ndarray``  

Usage
Installation
You can install the package directly from GitHub:

bash
Másolás
Szerkesztés
pip install git+https://github.com/Mart-SciecPyt/ScPytone_ultrasound_processing.git
Basic Usage Example
python
Másolás
Szerkesztés
import ultrasound_processing as upp
import matplotlib.pyplot as plt
import numpy as np

# Parameters
path = "input/cropped_frame_idx_50.png"
alpha_deg = 35
resolution = 50
alpha_rad = np.deg2rad(alpha_deg)

# Processing
transformed, depth, offset = upp.transform_curved_to_flat(path, alpha_deg, resolution)
masked = upp.remove_top_noise_and_keep_first_white(transformed)
final = upp.transform_flat_to_curved(masked, depth, alpha_rad, offset)

# Visualization
plt.imshow(final, cmap="gray")
plt.title("Final Processed Image")
plt.axis('off')
plt.show()

Available Functions

Function	Description
transform_curved_to_flat(path, alpha_deg, resolution)	Straightens curved ultrasound images
remove_top_noise_and_keep_first_white(image)	Removes noise and masks first white pixel contours
transform_flat_to_curved(image, depth, alpha_rad, offset)	Reprojects straightened images back to curved format
Input Parameters

Parameter	Type	Description
path	str	Path to the ultrasound image
alpha_deg	float	Half-angle of the device (degrees)
resolution	int	Pixel/cm resolution
depth	float	Depth of the image
offset	float	Offset from the source
Outputs
transformed : straightened image (np.ndarray)

masked : contour mask applied (np.ndarray)

final : reprojected curved image (np.ndarray)

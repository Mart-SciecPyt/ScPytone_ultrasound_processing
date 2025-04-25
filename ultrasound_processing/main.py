
import numpy as np
from .transform import transform
from .masking import mask
from .interpolation import interp_img

def process_ultrasound_image(path: str, alpha_deg: float = 35, resolution: float = 50, return_all=False):
    """
    Process an ultrasound image from curved to flat using transformation, masking, and interpolation.

    Args:
        path (str): Path to the input image.
        alpha_deg (float): Half angle of the ultrasound cone in degrees.
        resolution (float): Resolution factor for transformation.
        return_all (bool): If True, returns intermediate images as well.

    Returns:
        final_image (np.ndarray): The fully processed image.
        OR
        dict: If return_all=True, returns dictionary with all intermediate results.
    """
    alpha_rad = np.deg2rad(alpha_deg)

    # Step 1: Transform the curved image into flat
    transformed_image, depth, offset = transform(path, alpha_deg, resolution)

    # Step 2: Apply masking to remove top noise
    masked_image = mask(transformed_image)

    # Step 3: Interpolate the masked image back into a more natural-looking projection
    final_image = interp_img(masked_image, depth, alpha_rad, offset)

    if return_all:
        return {
            "transformed": transformed_image,
            "masked": masked_image,
            "final": final_image,
            "depth": depth,
            "offset": offset
        }
    return final_image

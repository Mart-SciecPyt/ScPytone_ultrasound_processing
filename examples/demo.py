
import ultrasound_processing as up
import matplotlib.pyplot as plt

flat = up.transform_curved_to_flat("ultrasound_processing/data/sample_curved_cropped_01.png")
_, _, _, masked = up.remove_top_noise_and_keep_first_white(flat)

plt.imshow(masked, cmap='gray')
plt.title("Processed Image")
plt.axis('off')
plt.show()

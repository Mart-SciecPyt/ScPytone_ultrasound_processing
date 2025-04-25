Usage
=====

Example:

.. code-block:: python

    import ultrasound_processing as up
    img = up.transform_curved_to_flat("ultrasound_processing/data/sample_curved_cropped_01.png")
    _, _, _, masked = up.remove_top_noise_and_keep_first_white(img)

    from matplotlib import pyplot as plt
    plt.imshow(masked, cmap='gray')
    plt.show()
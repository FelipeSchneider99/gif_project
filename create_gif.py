import imageio.v3 as iio


# List of sprite frame filenames in the order they should appear
# in the final animation.
filenames = []

# Container for loaded image frames
images = []

for filename in filenames:
    """
        Read each image file and append it to the images list.
        Path to the image file to be loaded.
        The image data is appended directly to the `images` list.
    """

    images.append(iio.imread(filename))

    """
    Write the collected frames to an animated GIF file.
    Output file path for the generated GIF.
        images : list
    Sequence of image arrays representing animation frames.
        duration : int
    Frame duration in milliseconds.
        loop : int
    Number of times the GIF should loop.
        0 means infinite looping.
    The GIF file is written to disk.
    """

iio.imwrite('', images, duration = 70, loop = 0)
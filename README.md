# Video Creation from Sorted Images

This script generates a video from a series of images stored in a specified directory. It arranges the images in numerical order based on an index extracted from their filenames and then compiles them into a video file.

## Prerequisites

- Python 3.x
- OpenCV (`cv2` Python library)

## Usage

1. Place your images in a directory.
2. Update the `image_folder` variable in the script with the path to your image directory.
3. Optionally, adjust the `video_name` variable to set the name of the output video.
4. Run the script.

## Script Overview

- The script first imports the required libraries: `cv2`, `os`, and `glob`.
- It sets the `image_folder` variable to the path of the directory containing the images.
- The `image_pattern` variable is created to define the file pattern for images (in this case, all `.jpg` files in the `image_folder`).
- Using `glob.glob()`, the script fetches a list of all image files that match the specified pattern.
- The list of image files is then sorted based on a numerical index extracted from the filenames.
- It initializes a video writer object with the dimensions of the first image.
- The script iterates through the sorted image files, reads each image, and writes it to the video file.
- Finally, it releases the video writer object and closes all OpenCV windows.

## Example

Suppose you have a directory named "images" containing a sequence of images named `0_image.jpg`, `1_image.jpg`, `2_image.jpg`, etc. Running the script with `image_folder = "images"` will produce a video file named `video.avi` in the same directory, containing the sorted and compiled images.

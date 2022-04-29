import cv2
import numpy as np


def detect_template(image_path, template_path):
    """detects pixel location of a template in an image

    Args:
        image_path (str): path to image file
        template_path (str): path to template file

    Returns:
        tuple[(int,int)]: a tuple of pixel location (x,y)
    """
    # Read the main image
    img_rgb = cv2.imread(image_path)

    # Convert it to grayscale
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

    # Read the template
    template = cv2.imread(template_path, 0)
    
    # Perform match operations.
    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)

    # Specify a threshold
    threshold = 0.8

    # Store the coordinates of matched area in a numpy array
    loc = np.where(res >= threshold)

    if len(loc[0]) != 1:
        return None

    return (loc[0][0], loc[1][0])

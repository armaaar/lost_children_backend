import base64
import cv2
from numpy import ndarray

def cv2_to_base64(cv_image: ndarray) -> str:
    """Convert cv2 to base64 string"""
    _, im_arr = cv2.imencode('.jpg', cv_image)  # im_arr: image in Numpy one-dim array format.
    return base64.b64encode(im_arr.tobytes()).decode('utf-8')

import cv2 as cv
import numpy as np
import base64
from io import BytesIO
from PIL import Image


def img_downsample(img, tgt_pixels):
    rtn = img.copy()
    actual_pixels = img.shape[0] * img.shape[1]
    if actual_pixels > tgt_pixels:
        ratio = (tgt_pixels / actual_pixels) ** 0.5
        w, h = int(img.shape[0] * ratio), int(img.shape[1] * ratio)
        rtn = cv.resize(img, (h, w))
    return rtn


def id_resize(img, tgt_pixels):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    actual_pixels = np.sum(gray > 0)
    ratio = (tgt_pixels / actual_pixels) ** 0.5
    w, h = int(img.shape[0] * ratio), int(img.shape[1] * ratio)
    rtn = cv.resize(img, (h, w))
    return rtn


def read_base64(base64_str):
    byte_data = base64.b64decode(base64_str)
    image_data = BytesIO(byte_data)
    return image_data


def base64_2_img(base64_str):
    img_buf = read_base64(base64_str)
    image = Image.open(img_buf)
    img = cv.cvtColor(np.asarray(image), cv.COLOR_RGB2BGR)
    return img


# image = Image.open("plane.jpg")
# image.show()
# img = cv2.cvtColor(numpy.asarray(image),cv2.COLOR_RGB2BGR)
# cv2.imshow("OpenCV",img)
# cv2.waitKey()

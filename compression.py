import PIL
from PIL import Image
import cv2

def compress(image):
    img = cv2.imread(image)
    height, width, _ = img.shape
    img = Image.open(image)
    img = img.resize((width,height),PIL.Image.ANTIALIAS)
    img.save('abc.jpg')


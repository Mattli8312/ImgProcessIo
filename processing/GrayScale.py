"""
GrayScale method for image processing
"""
from PIL import Image;

def GrayScale(image):
    w, h = image.width, image.height;
    result = Image.new(mode = "L", size = (w,h));
    for i in range(h):
        for j in range(w):
            rgba = image.getPixel(i,j);
            value = round(rgba[0] * 0.21 + rgba[1] * 0.7 + rgba[2] * 0.09);
            result.putpixel((j,i), (value));
    return result;
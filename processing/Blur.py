"""
Blurring method used for image processing 
Utilizing Gaussian Convolution using a Gaussian kernel
"""
import numpy as np;
import math;
from PIL import Image;
"""
G(x,y) = 1/(2 * pi * sigma**2) * exp(-(x**2 + y**2 / 2 * sigma**2))
@Todo
"""

def Gaussian_Helper(i, j, i_o, j_o, sigma):
    numerator = np.abs(i_o - i)**2 + np.abs(j_o - j)**2;
    return math.exp(-1 * numerator/(2 * sigma**2));

def Gaussian_Blur(image, sigma):
    w, h = image.getwidth, image.getheight;
    result = Image.new("L", (w,h));
    coefficient = 1 / (2 * np.pi * sigma**2);
    for i in range(h):
        for j in range(w):
            pass

def Regular_Blur(image):
    w, h = image.getwidth(), image.getheight();
    kernel_radius = 2;
    result = Image.new("RGB", (w,h));
    for i in range(h):
        for j in range(w):
            new_value_r = new_value_g = new_value_b = 0;
            for k in range(i - kernel_radius, i + kernel_radius + 1, 1):
                for l in range(j - kernel_radius, j + kernel_radius + 1, 1):
                    if k > 0 and k < h and l > 0 and l < w:
                        new_value_r = new_value_r + image.getPixel(k,l)[0];
                        new_value_g = new_value_g + image.getPixel(k,l)[1];
                        new_value_b = new_value_b + image.getPixel(k,l)[2];
            new_value_r = new_value_r // ((2 * kernel_radius + 1)**2);
            new_value_g = new_value_g // ((2 * kernel_radius + 1)**2);
            new_value_b = new_value_b // ((2 * kernel_radius + 1)**2);
            result.putpixel((j,i), (new_value_r, new_value_g, new_value_b));
    return result;
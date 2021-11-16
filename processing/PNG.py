import numpy as np;
from PIL import Image;
from processing import GrayScale as GS
from processing import Blur as BL
from processing import EdgeDetection as ED
from processing import Sharpen as SP

"""
PNG Class used for fetching data
"""

class PNG:
    def __init__(self, filename:str):
        self.image = Image.open('images/' + filename + '.png');
        self.width, self.height = self.image.size;
        self.picture_ = np.array([np.array([self.image.getpixel((w,h)) for w in range(self.width)]) for h in range(self.height)]);
        self.output_pic = None;
    """Utility functions"""
    def getwidth(self)->int:
        return self.width;

    def getheight(self)->int:
        return self.height;

    def getShape(self):
        return self.picture_.shape;

    def getPixel(self, i, j):
        return self.image.getpixel((j,i));

    def getImage(self):
        return self.image;

    def getOutput(self):
        return self.output_pic;

    def gray_scale(self):
        self.output_pic = GS.GrayScale(self);

    def blur_img(self):
        self.output_pic = BL.Regular_Blur(self);
    
    def edge_detection(self):
        self.output_pic = ED.Edge_detection_regular(self);

    def sharpen_image(self):
        self.output_pic = SP.Sharpen(self);

    def show_image(self):
        self.image.show();
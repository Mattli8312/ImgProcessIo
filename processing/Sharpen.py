from PIL import Image;
"""
Tool used for sharpening an image
"""

def Sharpen(image):
    kernel = [[0,-1,0],[-1,5,-1],[0,-1,0]];
    w,h = image.getwidth(), image.getheight();
    image.getImage().show();
    result = Image.new("RGB", (w,h));
    for i in range(h):
        for j in range(w):
            temp_val_r = temp_val_g = temp_val_b = 0;
            for k in range(3):
                for l in range(3):
                    if i - 1 + k > -1 and i - 1 + k < h and j - 1 + k > -1 and j - 1 + k < w:
                        temp_val_r = temp_val_r + kernel[k][l] * image.getPixel(i - 1 + k,j - 1 + k)[0];
                        temp_val_g = temp_val_g + kernel[k][l] * image.getPixel(i - 1 + k,j - 1 + k)[1];
                        temp_val_b = temp_val_b + kernel[k][l] * image.getPixel(i - 1 + k,j - 1 + k)[2];
            result.putpixel((j,i), (temp_val_r, temp_val_g, temp_val_b));
    return result;
import sys ; sys.path.append('./processing')
from processing import PNG;
test1 = PNG.PNG("amazon");
"""Test Bench"""

def main(argv):
    if(len(argv) != 3): 
        print("Invalid command: Should be $py main.py file function")
        return;
    file_name = argv[1];
    function = argv[2];
    test1 = PNG.PNG(file_name);
    if(function == "GrayScale"):
        test1.gray_scale();
    elif(function == "Blur"):
        test1.blur_img();
    elif(function == "Sharpen"):
        test1.sharpen_image();
    elif(function == "EdgeDetection"):
        test1.edge_detection();
    else:
        print("Invalid function: ");
        return;
    test1.getOutput().show();

if __name__ == "__main__": main(sys.argv);
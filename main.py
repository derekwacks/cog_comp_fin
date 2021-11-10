#from PIL import Image
import numpy as np
import cv2

def drawing_face():
    w, h = 512, 512
    data = np.zeros((h, w, 3), dtype=np.uint8)
    data[0:256, 0:256] = [255, 0, 0]
    img = Image.fromarray(data, 'RGB')
    img.save('my.png')
    img.show()


def image_to_grey(show_bool):
    """
    https://techtutorialsx.com/2019/04/13/python-opencv-converting-image-to-black-and-white/
    :return:
    """
    originalImage = cv2.imread('images/face2.jpg')
    greyImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
    # Note: try different thresholds here
    (thresh, blackAndWhiteImage1) = cv2.threshold(greyImage, 127, 255, cv2.THRESH_BINARY)

    if show_bool:
        cv2.imshow('Grey image', greyImage)
        cv2.imshow('Black white image', blackAndWhiteImage1)
        cv2.waitKey(0)  # closes windows when user presses key
        cv2.destroyAllWindows()

if __name__ == '__main__':
    image_to_grey(show_bool=True)
    print("complete")

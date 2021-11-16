#from PIL import Image
import numpy as np
import cv2
import face_maker

"""
def drawing_face():
    w, h = 512, 512
    data = np.zeros((h, w, 3), dtype=np.uint8)
    data[0:256, 0:256] = [255, 0, 0]
    img = Image.fromarray(data, 'RGB')
    img.save('my.png')
    img.show()
"""


def image_to_grey(show_bool):
    """
    https://techtutorialsx.com/2019/04/13/python-opencv-converting-image-to-black-and-white/
    :return: returning_images, list of all images as 2D numpy arrays
    """
    num_of_images = 2 # images currently in folder
    returning_images = []

    # Iterating over all images in folder
    for i in range(num_of_images):
        #file_name = 'images/face'+ str(i) +'.jpg'
        name = "images/face2.jpg"
        originalImage = cv2.imread(name)
        # Resizing to 250 x 250
        dim = (250,250)
        originalImage = cv2.resize(originalImage, dim)#, interpolation=cv2.INTER_AREA) # experiment with different interpolation methods
        greyImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
        # Note: try different thresholds here
        (thresh, blackAndWhiteImage1) = cv2.threshold(greyImage, 127, 255, cv2.THRESH_BINARY)

        if show_bool:
            cv2.imshow('Grey image', greyImage)
            cv2.imshow('Black white image', blackAndWhiteImage1)
            cv2.waitKey(0)  # closes windows when user presses key
            cv2.destroyAllWindows()

        # Convert all 255 values to 1's (so 2D array is binary)
        blackAndWhiteImage1[blackAndWhiteImage1 > 0] = 1
        # Add new image to list
        returning_images.append(blackAndWhiteImage1)
    return returning_images


if __name__ == '__main__':
    images = image_to_grey(show_bool=True)
    meta_data = [["Sam", '0'], ["Becca", '0']]

    data_frame = face_maker.create_dataframe()
    full_df = face_maker.fill_dataframe(data_frame, images, meta_data)
    print("in main full_df\n", full_df)

    #print("Checking...")
    #face_maker.check_created_file()

    print("Complete")
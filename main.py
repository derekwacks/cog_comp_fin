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


def image_to_grey(show_bool, num_of_images, face_type):
    """
    :param show_bool show images one at a time, as processed
    :param num_of_images number of images in folder
    :param face_type string, "masked" or "no_mask"

    https://techtutorialsx.com/2019/04/13/python-opencv-converting-image-to-black-and-white/
    :return: returning_images, list of all images as 2D numpy arrays
    """
    #num_of_images = 3 # images currently in folder, setting in main()
    returning_images = []

    # Iterating over all images in folder
    for i in range(num_of_images):
        #file_name = 'images/face'+ str(i) +'.jpg'

        name = "images/"+face_type+"/face"+str(i+1)+".jpg"
        print(name)
        originalImage = cv2.imread(name)
        # Resizing to 250 x 250
        dim = (150,150)
        originalImage = cv2.resize(originalImage, dim)#, interpolation=cv2.INTER_AREA) # experiment with different interpolation methods
        greyImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
        # Note: 125 threshold worked best (tried values between 100-200) such that
        # activity was primarily based on facial features (and not excessively on shadows)
        (thresh, blackAndWhiteImage1) = cv2.threshold(greyImage, 125, 255, cv2.THRESH_BINARY)

        if show_bool:
            cv2.imshow('greyscale image', greyImage)
            cv2.imshow('Black white image 135', blackAndWhiteImage1)
            cv2.waitKey(0)  # closes windows when user presses key
            cv2.destroyAllWindows()
            
        # Convert all 255 values to 1's (so 2D array is binary)
        blackAndWhiteImage1[blackAndWhiteImage1 > 0] = 1
        
        # Flip 0's and 1's
        blackAndWhiteImage1 = np.where((blackAndWhiteImage1 == 0) | (blackAndWhiteImage1 == 1), blackAndWhiteImage1 ^ 1, blackAndWhiteImage1)

        """
        # Convert all 255 values to 1's (so 2D array is binary)
        #blackAndWhiteImage1[blackAndWhiteImage1 > 0] = 1
        # Flip 0's and 1's
        blackAndWhiteImage1 = np.where((blackAndWhiteImage1 == 0) | (blackAndWhiteImage1 == 255), blackAndWhiteImage1 ^ 255,
                                       blackAndWhiteImage1)
        if show_bool:
            # cv2.imshow('Grey image', greyImage)
            cv2.imshow('greyscale image', greyImage)
            cv2.imshow('Black white image', blackAndWhiteImage1)
            cv2.waitKey(0)  # closes windows when user presses key
            cv2.destroyAllWindows()
        """

        # Add new image to list
        returning_images.append(blackAndWhiteImage1)
    return returning_images

def create_masked():
    images = image_to_grey(show_bool=True, num_of_images=num_of_images, face_type="masked")
    """
    meta_data_MASK_NOMASK = [["Sam", 'no-mask', 'happy'], ["Becca", 'no-mask', 'happy'], ["Jared", 'no-mask', 'happy'],
                 ["Sam", 'mask', 'happy'], ["Becca", 'mask', 'happy'], ["Jared", 'mask', 'happy']]

    meta_data_HAPPY_SAD = [["1", 'no-mask', 'happy'], ["2", 'no-mask', 'happy'], ["3", 'no-mask', 'happy'],
                 ["A", 'no-mask', 'sad'], ["B", 'no-mask', 'sad'], ["C", 'no-mask', 'sad']]
    """
    meta_data = []
    for i in range(6):
        person = [str(i + 1), 'no-mask', 'happy']
        meta_data.append(person)
    for i in range(6, 12):
        person = [str(i + 1), 'no-mask', 'sad']
        meta_data.append(person)
    masked_incl_bool = False  # don't include Masked column

    data_frame = face_maker.create_dataframe(dim, masked_incl_bool)
    full_df = face_maker.fill_dataframe(data_frame, images, meta_data, masked_incl_bool, face_file_name="masked_faces.tsv")
    return

def create_unmasked():
    images = image_to_grey(show_bool=True, num_of_images=num_of_images, face_type="no_mask")
    meta_data = []
    for i in range(6):
        person = [str(i + 1), 'no-mask', 'happy']
        meta_data.append(person)
    for i in range(6, 12):
        person = [str(i + 1), 'no-mask', 'sad']
        meta_data.append(person)
    masked_incl_bool = False  # don't include Masked column

    data_frame = face_maker.create_dataframe(dim, masked_incl_bool)
    full_df = face_maker.fill_dataframe(data_frame, images, meta_data, masked_incl_bool, face_file_name="no_mask_faces.tsv")
    return

if __name__ == '__main__':
    num_of_images = 12
    dim = 150
    """
    meta_data_MASK_NOMASK = [["Sam", 'no-mask', 'happy'], ["Becca", 'no-mask', 'happy'], ["Jared", 'no-mask', 'happy'],
                 ["Sam", 'mask', 'happy'], ["Becca", 'mask', 'happy'], ["Jared", 'mask', 'happy']]

    meta_data_HAPPY_SAD = [["1", 'no-mask', 'happy'], ["2", 'no-mask', 'happy'], ["3", 'no-mask', 'happy'],
                 ["A", 'no-mask', 'sad'], ["B", 'no-mask', 'sad'], ["C", 'no-mask', 'sad']]
    """
    #create_masked()
    create_unmasked()

    #face_maker.check_created_file()
    print("Complete")
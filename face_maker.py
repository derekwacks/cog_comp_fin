""""
import csv
tsv_file = open("example.tsv")
read_tsv = csv.reader(tsv_file, delimiter="\t")
"""
import pandas as pd
import numpy as np


path = "prev_code/face_categ/faces.tsv"
df = pd.read_csv(path, sep="\t")
a = df.values  # access array containing the values

"""
print(df)
print("Columns")
print(df.columns)
input_cols = [col for col in df.columns if 'Input' in col]
print(list(df.columns))
print(input_cols)
print("LEN", len(input_cols))
"""


# Creating new data frame
def create_dataframe(dim, mask_incl_bool):
    #new_data = {'_H:': [], '$Name': [], '%Masked[2:0,0]<2:1,2>': [], '%Masked[2:0,1]': [], '%Emotion[2:0,0]<2:1,2>': [], '%Emotion[2:0,1]': []}
    image = np.zeros((dim,dim))
    # happy = 1,0
    # sad = 0,1
    if mask_incl_bool:  # using Masked column and Emotion column
        new_data = {'_H:': [], '$Name': [], '%Masked[2:0,0]<2:1,2>': [], '%Masked[2:0,1]': [], '%Emotion[2:0,0]<2:1,2>': [], '%Emotion[2:0,1]': []}
    else:  # using just Output column as emotion column (and no Masked)
        new_data = {'_H:': [], '$Name': [], '%Output[2:0,0]<2:1,2>': [], '%Output[2:0,1]': []}
    for row in range(len(image)):  # 150 pixels
        for column in range(len(image[0])):  #150 pixels
            if row==0 and column==0:
                dims = str(dim)+","+str(dim)
                new_entry = "%Input[2:0,0]<2:"+dims+">"  # to match format in faces tsv
            else:
                new_entry = "%Input[2:"+str(row)+","+str(column)+"]"
            new_data[new_entry] = []  # Create new column in dataframe
    new_df = pd.DataFrame(data=new_data)
    return new_df



def fill_dataframe(data_frame, images, meta_data, mask_incl_bool, face_file_name):
    """
    :param data_frame: pandas data frame to fill with images (to eventually write to tsv)
    :param images: 2D numpy array filled with 0's and 255's
    :param meta_data: 2D array filled with names and info accompanying each image in 2D array
    :param mask_incl_bool: bool to include masked column for data
    :param face_file_name: tsv file name to write faces to
    :return: filled data_frame
    """
    print_check=False
    df_local_copy = data_frame.copy(deep=True)

    counter = 0
    for img in images:
        x = img.flatten()                   # flatten 2D numpy array
        y = list(map(str, x))               # convert to list of type str
        y.reverse()                         # corrects the orientation, so in the emergent network
                                            # the image is right-side-up
        if meta_data[counter][2] == "happy":
            y.insert(0, str(0))  # emotion indicator 0
            y.insert(0, str(1))  # emotion indicator 1
        elif meta_data[counter][2] == "sad":
            y.insert(0, str(1))  # emotion indicator 1
            y.insert(0, str(0))  # emotion indicator 0
        #y.insert(0, meta_data[counter][1])  # Masked or non-masked binary indicator
        if mask_incl_bool:  # If we're using the Masked column in the .dat/.tsv file
            if meta_data[counter][1] == "mask":
                y.insert(0, str(0))  # mask indicator 0
                y.insert(0, str(1))  # mask indicator 1
            elif meta_data[counter][1] == "no-mask":
                y.insert(0, str(1))  # mask indicator 1
                y.insert(0, str(0))  # mask indicator 0

        y.insert(0, meta_data[counter][0])  # Name
        y.insert(0, "_D:")                  # Row type (data or header)
        if print_check:
            print("in fill_df\n", y[:10])
            print("in fill_df\n", len(y))
            print(len(list(df_local_copy.columns)))
        new_row = pd.DataFrame([y], columns=list(df_local_copy.columns))
        df_local_copy = df_local_copy.append(new_row)
        counter+=1
    # Writing to tsv file
    df_local_copy.to_csv(face_file_name, index=False, sep='\t')

    return df_local_copy



def write_tsv(data_frame):
    """
    write filled data frame to TSV file to run in network
    :param data_frame: data frame to write
    :return: None
    """
    data_frame.to_csv('new_faces.tsv', index=False, sep='\t')
    print("New face tsv file created!")

def check_created_file():
    check = pd.read_csv("new_faces.tsv", sep="\t")
    #a = check.values  # access array containing the values
    print(check)

def create_test_plot():
    ret = np.zeros(shape=(10,10))
    ret[:,1] = 1
    ret[8,:] = 1
    return ret


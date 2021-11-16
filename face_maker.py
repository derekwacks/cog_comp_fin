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
def create_dataframe():
    image = np.zeros((250,250))
    new_data = {'_H:': [], '$Name': [], '%Masked': []}
    for row in range(len(image)):  # 250 pixels
        for column in range(len(image[0])):  # 250 pixels
            if row==0 and column==0:
                new_entry = "%Input[2:0,0]<2:250,250>"  # to match format in faces tsv
            else:
                new_entry = "%Input[2:"+str(row)+","+str(column)+"]"
            new_data[new_entry] = []  # Create new column in dataframe
    new_df = pd.DataFrame(data=new_data)
    return new_df



def fill_dataframe(data_frame, images, meta_data):
    """
    :param data_frame: pandas data frame to fill with images (to eventually write to tsv)
    :param images: 2D numpy array filled with 0's and 255's
    :param meta_data: 2D array filled with names and info accompanying each image in 2D array
    :return: filled data_frame
    """
    print_check=False
    df_local_copy = data_frame.copy(deep=True)

    counter = 0
    for img in images:
        x = img.flatten()                   # flatten 2D numpy array
        y = list(map(str, x))               # convert to list of type str
        y.insert(0, meta_data[counter][1])  # Masked or non-masked binary indicator
        y.insert(0, meta_data[counter][0])  # Name
        y.insert(0, "_D:")                  # Row type (data or header)
        if print_check:
            print("in fill_df\n", y[:10])
            print("in fill_df\n", len(y))
            print(len(list(df_local_copy.columns)))
        new_row = pd.DataFrame([y], columns=list(df_local_copy.columns))
        df_local_copy = df_local_copy.append(new_row)
        counter+=1

    #write_tsv(data_frame)
    # calling here instead
    df_local_copy.to_csv('new_faces.tsv', index=False, sep='\t')

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
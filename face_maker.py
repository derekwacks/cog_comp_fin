
""""
import csv
tsv_file = open("example.tsv")
read_tsv = csv.reader(tsv_file, delimiter="\t")
"""


import pandas as pd
import numpy as np

# make a dummy .tsv file, save it to disk
#dummy = pd.DataFrame(np.random.randint(0,10,(200,100)))
#save_path = "foo.tsv"
#dummy.to_csv(save_path, index=False, sep="\t")

path = "prev_code/face_categ/faces.tsv"
df = pd.read_csv(path, sep="\t")   # read dummy .tsv file into memory
a = df.values  # access the numpy array containing values
print(df.columns)

input_cols = [col for col in df.columns if 'Input' in col]
print(list(df.columns))
print(input_cols)
print("LEN", len(input_cols))


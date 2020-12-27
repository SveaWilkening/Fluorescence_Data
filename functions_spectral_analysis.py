import os
import pandas as pd
import numpy as np

### function to import data and generate dataframe###
def generate_df(data_path):
    files_col = []  #list to store filenames, for column naming 
    filenames = []  #list to store files for reading them into a df

    for root, dirs, files in os.walk(data_path):
        for file in files:
            if file.endswith(".PRN"):
                files_col.append(str(file.split(".")[0]))
                filenames.append(os.path.join(data_path, root, str(file)))

    li = []

    for filename in filenames:
        df = pd.read_csv(filename, sep="\t", header=None)
        li.append(df)

    frame = pd.concat(li, axis=1, ignore_index=True)

    n = 2
    files_col = list(np.repeat(files_col, n))

    frame.columns = files_col

    return frame


def generate_df_dat(data_path):
    datfiles = []
    datfiles_names = []

    for root, dirs, files in os.walk(data_path):
        for file in files:
            if file.endswith(".dat"):
                datfiles.append(os.path.join(data_path, root, str(file)))
                datfiles_names.append(str(file.split(".")[0]))

    li = []

    for filename in datfiles:
        df = pd.read_csv(filename,skiprows=(1), sep="\s+")
        li.append(df)
        
    frame = pd.concat(li, axis=1, ignore_index=True)
    
    n = 2
    files_col = list(np.repeat(datfiles_names,n))
    
    frame.columns = files_col
    
    #add x-values from 0- 20 ns
    x = np.linspace(0,20,4095)
    frame['x'] = x
    
    return frame

 #separate long and short excitation data
def separate_long_short(dataframe):
    short = dataframe.loc[:,~dataframe.columns.str.contains('L', case=False)]

    long = dataframe.loc[:,dataframe.columns.str.contains('L', case=False)]

    return short, long

def separate_x_y(dataframe):

    x_frame = dataframe.iloc[:,0]
    x_frame = x_frame.rename("x")

    y_frame = dataframe.iloc[:,1::2]

    frames = [x_frame,y_frame]

    df_x = pd.concat(frames, axis=1)

    return df_x


def rename_cols(dataframe):

    dataframe.columns = dataframe.columns.str.replace("UM", "")
    dataframe.columns = dataframe.columns.str.replace("L", "")

    return dataframe


#scale y-axis data
def scale_y_axis(dataframe, col_list):
    for i in col_list:
        dataframe[i] /= 10000
    return dataframe




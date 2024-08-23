#https://www.python.org/downloads/release/python-379/





folder="set PATH="



import os
import pandas as pd


all_files = os.listdir(folder)
all_files = [os.path.join(folder,f) for f in all_files]



def read_data(filepath, sheet_name = 1, columns = None):
    #filepath = "xxxx"
    #columns = ['A', 'B']
    df = pd.read_excel(filepath, sheet_name=1)
    if columns:
        df = df[columns]
    return df


df_list = []
for filepath in all_files:
    df = read_data(filepath, sheet_name = 1, columns = None)
    df_list.append(df)

df_all = pd.concat(df_list, ignore_index=True, sort=False)
df_all.to_excel("output_file.xlsx")



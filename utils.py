import os
import pandas as pd

def explore_data(folder_path, file_name):
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        df = pd.read_csv(file_path)
    
    # Data preprocessing
    len1 = df.drop_duplicates()

    # data = []
    # for i in range(len(df)):
    #     data.append(df.iloc[i,:].tolist())

    # return df.columns.tolist(), data

    return len(df), len(len1)
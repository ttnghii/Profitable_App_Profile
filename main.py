from utils import explore_data


# Import dataset
folder_path = 'dataset'

android_app, android = explore_data(folder_path=folder_path, file_name='GooglePlayStore.csv')    
ios_app, ios = explore_data(folder_path=folder_path, file_name='AppleStore.csv')


# Data Cleaning

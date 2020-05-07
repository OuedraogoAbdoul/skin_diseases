# Import neccessary libraries
import config
import os
from glob import glob
import pandas as pd


def create_dataset(dataset_folder):
    """Load images and create a dataframe

    """
    image_df = []
    for image_folders in os.listdir(dataset_folder):

        for image_path in glob(os.path.join(os.path.join(dataset_folder, image_folders), "*.jpg")):
            tmp = pd.DataFrame([image_path, image_folders]).T
            image_df.append(tmp)

    image_df = pd.concat(image_df, axis=0, ignore_index=True)
    image_df.columns = ['image_paths', 'classes']


    return image_df


def split_dataset(df):
    """"Split the dataset into train, test

    """

    return 


def save_model(model):
    """"Save trained models

    """
    pass


def load_trained_model():

    pass

if __name__ == '__main__':

    df = create_dataset(config.DATA_PATH)
    print(f"Sample image dataframe {df.sample(5)}")
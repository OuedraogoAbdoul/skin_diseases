# Import neccessary libraries
import config
import os
from glob import glob
import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np


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
    # X_train, X_test, y_train, y_test = train_test_split(df["image_paths"], df["classes"], test_size=0.20, random_state=42)
    train, validate, test = np.split(df.sample(frac=1), [int(.94*len(df)), int(.96*len(df))])
    return  train, validate, test


def save_model(model):
    """"Save trained models

    """
    pass


def load_trained_model():

    pass

if __name__ == '__main__':

    df = create_dataset(config.DATA_PATH)
    train, validate, test = split_dataset(df)
    print(f"Sample image dataframe {df.shape}")
    print(f"Training set size {train.shape}, Test set size {test.shape, test.shape}, validation {validate.shape}")
    print(train["image_paths"])
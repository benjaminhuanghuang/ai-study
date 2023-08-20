'''
    From Hands-On Machine Learning with Scikit-Learn and TensorFlow Ch2
    
    It's a dome of 
        from sklearn.model_selection import train_test_split
        train_set, test_set = train_test_split(housing, test_size=0.2, random_state=42)

    train_test_split does pretty much the same thing as  split_train_test defined
'''

import os
import tarfile
from six.moves import urllib
import pandas as pd
import numpy as np
import hashlib
from sklearn.model_selection import train_test_split


DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml/master/"
HOUSING_PATH = "data/housing"
HOUSING_URL = DOWNLOAD_ROOT + HOUSING_PATH + "/housing.tgz"


def load_housing_data(housing_path=HOUSING_PATH):
    csv_path = os.path.join(housing_path, "housing.csv")
    return pd.read_csv(csv_path)

def split_train_test(data, test_ratio):
    np.random.seed(42) # Always generates same shuffled indeices
    shuffled_indices = np.random.permutation(len(data))   # Create random shuffled indeices
    test_set_size = int(len(data) * test_ratio)
    test_indices = shuffled_indices[:test_set_size]
    train_indices = shuffled_indices[test_set_size:]
    return data.iloc[train_indices], data.iloc[test_indices]

def test_set_check(identifier, test_ratio, hash):
    return hash(np.int64(identifier)).digest()[-1] < 256 * test_ratio


def split_train_test_by_id(data, test_ratio, id_column, hash=hashlib.md5):
    '''
        Use id column to keep test set consistent across multiple runs, even if you refresh the dataset.
        Create id for row: housing_with_id["id"] = housing["longitude"] * 1000 + housing["latitude"]
    '''
    ids = data[id_column]
    in_test_set = ids.apply(lambda id_: test_set_check(id_, test_ratio, hash))
    return data.loc[~in_test_set], data.loc[in_test_set]

if __name__ == '__main__':
    housing = load_housing_data()
    housing_with_id = housing.reset_index() # adds an `index` column
    housing_with_id["id"] = housing["longitude"] * 1000 + housing["latitude"]
    train_set, test_set = split_train_test_by_id(housing_with_id, 0.2, "id")

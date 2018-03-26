'''
    From Hands-On Machine Learning with Scikit-Learn and TensorFlow Ch2

    Data information
       - Each row represents one district. There are 10 attributes : 
            longitude, latitude, housing_median_age, total_rooms, total_bedrooms, 
            population, households, median_income, median_house_value, and ocean_proximity.
'''

import os
import tarfile
from six.moves import urllib
import pandas as pd

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml/master/"
HOUSING_PATH = "data/housing"
HOUSING_URL = DOWNLOAD_ROOT + HOUSING_PATH + "/housing.tgz"


def fetch_housing_data(housing_url=HOUSING_URL, housing_path=HOUSING_PATH):
    ''' 
        Create data/housing folder
        Download housing.tgz
        Extract housing.cvs
    '''
    if not os.path.isdir(housing_path):
        os.makedirs(housing_path)
    tgz_path = os.path.join(housing_path, "housing.tgz")
    urllib.request.urlretrieve(housing_url, tgz_path)
    housing_tgz = tarfile.open(tgz_path)
    housing_tgz.extractall(path=housing_path)
    housing_tgz.close()


def load_housing_data(housing_path=HOUSING_PATH):
    csv_path = os.path.join(housing_path, "housing.csv")
    return pd.read_csv(csv_path)


if __name__ == '__main__':
    housing = load_housing_data()
    print('Head of data', housing.head())   # 5 rows
    print('Data information', housing.info())   
    # find value ategories of feature
    print('Value categories of ocean_proximity', housing['ocean_proximity'].value_counts())
    print('Data description', housing.describe())    # statistic information
    
    housing.hist(bins=50, figsize=(20,15))
    plt.show()
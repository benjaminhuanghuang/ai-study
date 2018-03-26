'''
    From Hands-On Machine Learning with Scikit-Learn and TensorFlow Ch2
    https://github.com/ageron/handson-ml/blob/master/02_end_to_end_machine_learning_project.ipynb
    
    Data information
       - Each row represents one district. There are 10 attributes : 
            longitude, latitude, housing_median_age, total_rooms, total_bedrooms, 
            population, households, median_income, median_house_value, and ocean_proximity.
'''

import os
import tarfile
from six.moves import urllib
import pandas as pd
import numpy as np
from sklearn.model_selection import StratifiedShuffleSplit

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

    # print('Head of data', housing.head())   # 5 rows
    # print('Data information', housing.info())   
    # # find value ategories of feature
    # print('Value categories of ocean_proximity', housing['ocean_proximity'].value_counts())
    # print('Data description', housing.describe())    # statistic information
    
    # housing.hist(bins=50, figsize=(20,15))
    # plt.show()

    housing["income_cat"] = np.ceil(housing["median_income"] / 1.5)
    # merging all the categories greater than 5 into category 5
    housing["income_cat"].where(housing["income_cat"] < 5, 5.0, inplace=True)
    '''
    The test set generated using stratified sampling has income category proportions almost identical to those 
    in the full dataset, whereas the test set generated using purely random sampling is quite skewed.
    '''
    split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
    for train_index, test_index in split.split(housing, housing["income_cat"]):
        strat_train_set = housing.loc[train_index]
        strat_test_set = housing.loc[test_index]

    for set in (strat_train_set, strat_test_set):
        set.drop(["income_cat"], axis=1, inplace=True)

    housing = strat_train_set.copy()
    # Plot the locations of the houses
    # housing.plot(kind="scatter", x="longitude", y="latitude", alpha=0.1)

    '''
        A better scatter plot
        The radius of each circle represents the district’s population (option s), 
        and the color represents the price (option c). 
        We will use a predefined color map (option cmap) called jet, which ranges from blue (low values) to red (high prices):
    '''
    housing.plot(kind="scatter", x="longitude", y="latitude", alpha=0.4, s=housing["population"]/100, label="population",
                    c="median_house_value", cmap=plt.get_cmap("jet"), colorbar=True )
    plt.legend()
        
    # plt.show()
    # compute the standard correlation coefficient  between every pair of attributes
    corr_matrix = housing.corr()
    #how much each attribute correlates with the median house value:
    print('attribute correlates with the median house value', corr_matrix["median_house_value"].sort_values(ascending=False))
from ctypes.wintypes import PSIZEL
import os
import tarfile
import urllib.request
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import StratifiedShuffleSplit

#revisar por que no esta descargando el archivo
DOWNLOAD_ROOT = "https://github.com/ageron/handson-ml2/blob/master/"
HOUSING_PATH = os.path.join("datasets", "housing")
HOUSING_URL =  DOWNLOAD_ROOT + "datasets/housing/housing.tgz"

def fetch_housing_data(housing_url=HOUSING_URL, housin_path=HOUSING_PATH):
    os.makedirs(housin_path, exist_ok=True)
    tgz_path = os.path.join(housin_path, "housing.tgz")
    urllib.request.urlretrieve(housing_url, tgz_path)
    housing_tgz = tarfile.open(tgz_path)
    housing_tgz.extractall(path=housin_path)
    housing_tgz.close()

def load_housing_data(housing_path=HOUSING_PATH):
    csv_path = os.path.join(housing_path, "housing.csv")
    return pd.read_csv(csv_path)

def split_train_test(data, test_ratio):
    shuffled_indicates = np.random.permutation(len(data))
    test_set_size = int(len(data) * test_ratio)
    test_indices = shuffled_indicates[:test_set_size]
    train_indices = shuffled_indicates[test_set_size:]
    return data.iloc[train_indices], data.iloc[test_indices]
    
def stratify_shuffle_split(data):
    split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
    for train_index, test_index in split.split(data, data["income_cat"]):
        strat_train_set = housing.loc[train_index]
        strat_test_set = housing.loc[test_index]
        test = strat_test_set["income_cat"].value_counts() / len(strat_test_set)
        print(test)

    
if __name__ == '__main__':
    housing = load_housing_data()
    # print(housing.info())
    # print(housing["ocean_proximity"].count())
    # print(housing.describe())
    
    # housing.hist(bins=50,  figsize=(20,15))
    # plt.show()
    
    # train_set, test_set = split_train_test(housing, 0.2)
    # housing["income_cat"] = pd.cut(housing["median_income"], bins=[0., 1.5, 3.0, 4.5, 6., np.inf], 
    #                                labels=[1, 2, 3, 4, 5])
    
    # stratify_shuffle_split(housing)
    # housing["income_cat"].hist()    
    # plt.show()
    
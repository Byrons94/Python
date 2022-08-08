from cProfile import label
from ctypes.wintypes import PSIZEL
import os
import tarfile
import urllib.request
from attr import attributes
from matplotlib.cm import get_cmap
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pyparsing import alphas
from sklearn.model_selection import StratifiedShuffleSplit
from pandas.plotting import scatter_matrix

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
    #cut data in new column
    data["income_cat"] = pd.cut(data["median_income"], bins=[0., 1.5, 3.0, 4.5, 6., np.inf], 
                                labels=[1, 2, 3, 4, 5])
     
     
    split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
    for train_index, test_index in split.split(data, data["income_cat"]):
        strat_train_set = data.loc[train_index]
        strat_test_set = data.loc[test_index]
        test = strat_test_set["income_cat"].value_counts() / len(strat_test_set)
        return strat_train_set, strat_test_set
        
# plot showing price per region and population in california
def plot_price_region_population(train_data): 
    train_data.plot(kind="scatter", x="longitude", y="latitude", alpha=0.4,
                    s=train_data["population"]/100, label="population", figsize=(10, 7), 
                    c="median_house_value", cmap=plt.get_cmap("jet"), colorbar=True)
    plt.legend()

#set and prints the standard correlation in the train set
def standard_correlation_coefficient(train_data):
    corr_matrix = train_data.corr()
    corr_matrix_sorted = corr_matrix["median_house_value"].sort_values(ascending=False)
    print(corr_matrix_sorted)
 
 #shows a scatter_matrix of the most promising attributes
 #plots every numerical attribute agains every other numerical attribute, plus and histogram of each numerical attribute
def scatter_matrix_train(train_data):
    attributes = ["median_house_value", "median_income", "total_rooms", "housing_median_age"]
    scatter_matrix(train_data[attributes], figsize=(12, 8))
    
#shows a scatter plot of the median income * median_house_value
def median_income_plot(train_data):
    train_data.plot(kind="scatter", x="median_income", y="median_house_value", alpha=0.1)        

#experimenting new attributes to see correlation
def experimenting_with_attributes(train_data):
    train_data["rooms_per_household"] = train_data["total_rooms"] / train_data["households"]
    train_data["bedrooms_per_room"] = train_data["total_bedrooms"] / train_data["total_rooms"]
    train_data["population_per_house"] = train_data["population"] / train_data["households"]
    corr_matrix = train_data.corr()
    corr_matrix_sorted = corr_matrix["median_house_value"].sort_values(ascending=False)
    print(corr_matrix_sorted)
 
if __name__ == '__main__':
    housing = load_housing_data()
    
    # housing["income_cat"].hist()    
    # plt.show()
    
    
    #gets data splited 80/20
    splited_data = stratify_shuffle_split(housing)
    train_data = splited_data[0].copy()
    test_data = splited_data[1].copy()
    
    #example of population in california
    # train_data.plot(kind="scatter", x="longitude", y="latitude", alpha=0.1)
    
    experimenting_with_attributes(train_data)
    
    plt.show()    
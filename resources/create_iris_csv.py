""" Create CSV file for Iris dataset

For the svm tutorial, only a subset of the Iris dataset provided by sklearn is 
used. This script creates a CSV file with the subset of the Iris dataset.
"""

import pandas as pd
from sklearn import datasets

# load Iris dataset
dict = datasets.load_iris()
# create dataframe from dict
df = pd.DataFrame(dict['data'], columns=dict['feature_names'])
# add target column
df['species'] = dict['target']

# first dataframe: only 2 features
df1 = df[['species', 'sepal length (cm)', 'sepal width (cm)']]
# reduce to 2 classes
df1 = df1.loc[df1['species'] != 2].reindex()
# substitute species values with names
df1 = df1.replace({'species': {0: 'setosa', 1: 'versicolor'}})

# save dataframe 1 to CSV
df1.to_csv('resources/iris.csv', index=False)

# Data Preprocessing Template

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values

print "independent variables"
print X
print "dependent variable"
print y

#Take care of missing data, axis=0 impute along columns
from sklearn.preprocessing import Imputer
imputer= Imputer(missing_values= 'NaN', strategy= 'mean', axis= 0)
imputer= imputer.fit(X[:,1:3])
X[:,1:3]= imputer.transform(X[:,1:3])

#new X matrix with missing data replaced by mean values
print X

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
#
labelencoder_X = LabelEncoder()
X[:, 0] = labelencoder_X.fit_transform(X[:, 0])

print X
# Dummy Encoding
onehotencoder = OneHotEncoder(categorical_features = [0])
X = onehotencoder.fit_transform(X).toarray()
# Encoding the Dependent Variable
labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)

print X
print y

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
#20% test cases and rest train sets
print X_train
print X_test
print y_train
print y_test

# Feature Scaling i.e. bring the test set cases values in same range [-1,1]
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
# not for y since it is categorial
#import libraries
import numpy as np
import matplotlib.pylot as plt
import pandas as pd 

dataset = pd.read_csv('Data.csv')
#take all rows, take all columns except last
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values

from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
imputer = imputer.fit(x[:, 1:3])
x[:, 1:3] = imputer.transform(x[:, 1:3])

#encode categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelEncoder_x = LabelEncoder()
x[:, 0] = labelEncoder_x.fit_transform(x[:, 0]) 
onehotencorder = OneHotEncoder(categorical_features = [0])
x = onehotencoder.fit_transform(x).toarray()
#prevent encoding from giving higher val to one cat
labelEncoder_y = LabelEncoder()
y = onehotencoder.fit_transform().toarray()
#encode "purchased" coulumn
labelEncoder_y = LabelEncoder()
y = labelEncoder_x.fit_transform(y)

#splitting
from sklearn.cross_validation import train_test_split
xtrain, xtest, ytrain, ytest = train_test_split(x,y, test_size = 0.2, random_state = 0)

#feature scaling
from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
x_train = sc_x.fit_transform(x_train)
x_test = sc_x.fit_transform(x_test)



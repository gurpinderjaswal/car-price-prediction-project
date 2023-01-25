import pandas as pd


from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

from sklearn import metrics

# loading the data from csv file to pandas dataframe
car_dataset = pd.read_csv('cardata.csv')

#Encoding the Categorical Data

# encoding "Fuel_Type" Column
car_dataset.replace({'Fuel_Type':{'Petrol':0,'Diesel':1,'CNG':2}},inplace=True)

# encoding "Seller_Type" Column
car_dataset.replace({'Seller_Type':{'Dealer':0,'Individual':1}},inplace=True)

# encoding "Transmission" Column
car_dataset.replace({'Transmission':{'Manual':0,'Automatic':1}},inplace=True)

#Splitting the data and Target

X = car_dataset.drop(['Car_Name','Selling_Price'],axis=1)
Y = car_dataset['Selling_Price']

#Splitting Training and Test data

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.1, random_state=42)

#Applying Random Forest Regression Algo

from sklearn.ensemble import RandomForestRegressor

regressor = RandomForestRegressor(n_estimators=200, random_state=42)
regressor.fit(X_train, Y_train)
Y_pred = regressor.predict(X_test)
'''

#Linear LinearRegression
from sklearn.linear_model import LinearRegression

lin_reg_model = LinearRegression()
lin_reg_model.fit(X_train,Y_train)
'''
#import pickle
import pickle
pickle.dump(regressor, open('model.pkl','wb'))
model = pickle.load(open('model.pkl','rb')) 
#taking third row for analysing
#print(model.predict([[2009,85,11,87934,0,0,0,0]]))













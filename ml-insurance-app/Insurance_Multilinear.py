"""
Created on Wed Jun 18 11:37:28 2025

@author: abinnu
"""

import pandas as pd 
import numpy as np 

Data = pd.read_csv("D:/project_linear_regression/dataset/insurance.csv")
Data.head()

Data.isnull().sum()


Data = pd.get_dummies(Data,columns=["sex","smoker","region"],drop_first=True)


X = Data.drop("charges",axis = 1)
Y = Data["charges"]



from sklearn.model_selection import train_test_split

xtrain,xtest,ytrain,ytest = train_test_split(X,Y,test_size=0.2,random_state=0)



from sklearn.linear_model import LinearRegression 

model = LinearRegression()
model.fit(xtrain,ytrain)
import joblib
joblib.dump(model,"D:/project_linear_regression/deployment/ml-insurance-app/model/multilinear.pkl")


ypred = model.predict(xtest)
ypred


from sklearn.metrics import mean_absolute_error

MAE = mean_absolute_error(ytest,ypred)
MAE


from sklearn.metrics import mean_squared_error

MSE = mean_squared_error(ytest,ypred)
MSE


from sklearn.metrics import r2_score

R2score = r2_score(ytest,ypred)
R2score



import numpy
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('Salary_Data.csv')
print(dataset.head())

#Independent Variable
X = dataset.iloc[:,:-1].values
#Dependent Variable
Y = dataset.iloc[:,1].values


#Splitting datasets
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size =1/3, random_state=0)

#Fitting to the regression line
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, Y_train)

#Predicting Values
Y_pred = regressor.predict(X_test)
print(Y_pred)
print(Y_test)

#Plotting for TRAIN|
plt.scatter(X_train, Y_train, color='red')
plt.plot(X_train, regressor.predict(X_train), color='blue')
plt.title('Salary vs Experience (Training Set)')
plt.xlabel('Years of experience')
plt.ylabel('Salary')
#Plotting for TEST
plt.show()

plt.scatter(X_test, Y_test, color='brown')
plt.plot(X_train, regressor.predict(X_train), color = 'gray')
plt.xlabel('Years of experience')
plt.ylabel('Salary')
plt.show()
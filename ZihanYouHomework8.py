#Zihan You Homework 8 - Final Project
houseFileName = 'C:/Users/zihan/Downloads/House Prices.csv'
newHouseFileName = 'C:/Users/zihan/Downloads/House Prices New.csv'

import pandas as pd
from pandas import DataFrame
from sklearn import linear_model

housePriceDF = pd.read_csv(houseFileName, header = 0)
newHousePriceDF = pd.read_csv(newHouseFileName, header = 0)

#Use House Price Data to build a multiple linear regression by sklearn
#This block came from https://datatofish.com/multiple-linear-regression-python/
X = housePriceDF[['Property Size (acres)', 'House Size (square feet)', 'Age', 'Rooms', 'Garage','Baths']]
Y = housePriceDF['Appraised Value']

regr = linear_model.LinearRegression()
regr.fit(X, Y)
print('Intercept: \n', regr.intercept_) #Intercept: 83.06068899170748
print('Coefficients: \n', regr.coef_)
#Coefficients: 2.92170869e+02  1.00578552e-01 -1.25333190e+00  1.06893175e+01 1.59765791e+01  6.27807820e+00
#End of code from https://datatofish.com/multiple-linear-regression-python/

#Use the intercept and the coefficient to build a function
#This function can calculate the house price
def calculateHousePrice(pSize,hSize,Age,Rooms,Garage,Baths):
    housePrice = 83.06068899170748 + 2.92170869e+02*pSize + 1.00578552e-01*hSize +(-1.25333190e+00)*Age + 1.06893175e+01*Rooms + 1.59765791e+01*Garage + 6.27807820e+00*Baths
    return housePrice

#User can input new data into dataframe
enterAddress = input('Please enter the Address:\n')

#Error handling, PropertySize and HouseSize need to be float or integer
enterPropertySize  = input('Please enter the Property Size (acres):\n')
try:  
    enterPropertySize = float(enterPropertySize)
except ValueError:
    input('Could not convert string to float,Please enter property size without unit:\n')
enterHouseSize = input('Please enter the House Size (square feet):\n')
try:  
    enterHouseSize = float(enterHouseSize)
except ValueError:
    input('Could not convert string to float,Please enter house size without unit:\n')
    
enterAge = input('Please enter the Age:\n')
enterRooms = input('Please enter the number of Rooms:\n')
enterGarage = input('Please enter the number of Garage:\n')
enterBaths = input('Please enter the number of Baths:\n')

newHousePriceDF.loc[newHousePriceDF.shape[0]+1]=({'Address': enterAddress, 'Property Size (acres)': enterPropertySize, 'House Size (square feet)': enterHouseSize,'Age':float(enterAge),'Rooms':float(enterRooms),'Garage':float(enterGarage),'Baths':float(enterBaths)})

#Calculate the house price in new dataset
predictedPriceList = []
CategoryList = []
for i in range(0,newHousePriceDF.shape[0]):
    lineList = newHousePriceDF.iloc[i].tolist()
    pSize = lineList[1]
    hSize = lineList[2]
    Age = lineList[3]
    Rooms = lineList[4]
    Garage = lineList[5]
    Baths = lineList[6]
    predictedPrice = calculateHousePrice(pSize,hSize,Age,Rooms,Garage,Baths)
    if predictedPrice >= 400:
        Category = 'high' #which indicates its a high price
    elif predictedPrice >= 300:
        Category = 'medium' #which indicates its a medium price
    else:
        Category = 'low' #which indicates its a low price
    predictedPriceList.append(predictedPrice)
    CategoryList.append(Category)

#Add new columns to dataframe
newHousePriceDF['predictedPrice'] = predictedPriceList
newHousePriceDF['Category'] = CategoryList

#Export the dataframe to a CSV file
newHousePriceDF.to_csv('C:/Users/zihan/Downloads/PredictedHousePrices.csv', index=False)

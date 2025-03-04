import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

#loading the dataset using pandas
data = pd.read_csv("C:/Users/KB.com/OneDrive/Pictures/Mabonono/Internship Tasks/cognify internship/Dataset .csv")

#dropping irrelevant columns within the dataset
dropColumns = ["Restaurant ID", "Restaurant Name", "Address", "Locality", 
               "Locality Verbose", "Rating color", "Rating text", "Country Code", "City", "Currency"]
dataCleaned = data.drop(columns = dropColumns)

#handling missing values
dataCleaned = dataCleaned.dropna()

#print(dataCleaned.isnull().sum())

#creading an empty dictionary for storing encoded values 
labelEncoders = {}

#creating a list of all of the categorical columns that will be encoded
relevantColumns = ["Cuisines", "Has Table booking", "Has Online delivery", "Is delivering now", "Switch to order menu"]
#using the for loop to iterate through the list of categorical columns 
for column in relevantColumns:
    #assigning the variable encoder to the LabelEncoder() method for changing the categorical values into numeric values
    encoder = LabelEncoder()
    #transforming the categorical values that are from the cleaned dataset into numerical values and re-assigning/replacing them to the exact/same location, but this time as numeric values
    dataCleaned[column] = encoder.fit_transform(dataCleaned[column])
    #filling in all of the encoded values into the empty dictionary created
    labelEncoders[column] = encoder
    #outputting all of the encoded values for each column
    print("------------------------------------------------------------------------------")
    print("------------------ENCODED VALUES FOR ", column, "----------------------")
    print("------------------------------------------------------------------------------")
    print(dataCleaned[relevantColumns])
    
#creating the x-variable for holding all of the cleaned data except for the Aggregate rating column
x = dataCleaned.drop(columns = ["Aggregate rating"])
#assigning the Aggregate column to the y-variable
y = dataCleaned["Aggregate rating"]

#outputting the columns within the x variable
print("------------------------------------------------------------------------------")
print("--------------------COLUMNS WITHIN THE X-VARIABLE-----------------------------")
print("------------------------------------------------------------------------------")
print(x)
print("------------------------------------------------------------------------------")
#outputting the columns within the y variable
print("--------------------COLUMNS WITHIN THE Y-VARIABLE-----------------------------")
print("------------------------------------------------------------------------------")
print(y)
print("------------------------------------------------------------------------------")

#splitting the dataset into both train and test sets
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 0.2, random_state = 42)
#outputting the columns and values within the x_train
print("----------------------COLUMNS WITHIN THE X-TRAIN------------------------------")
print("------------------------------------------------------------------------------")
print(x_train)
print("------------------------------------------------------------------------------")
#outputting the columns and values within the x_test
print("----------------------COLUMNS WITHIN THE X-TEST------------------------------")
print("------------------------------------------------------------------------------")
print(x_test)
print("------------------------------------------------------------------------------")
#outputting the columns and values within the y_train
print("----------------------COLUMNS WITHIN THE Y-TRAIN------------------------------")
print("------------------------------------------------------------------------------")
print(y_train)
print("------------------------------------------------------------------------------")
#outputting the columns and values within the y_test
print("----------------------COLUMNS WITHIN THE Y-TEST------------------------------")
print("------------------------------------------------------------------------------")
print(y_test)
print("------------------------------------------------------------------------------")

#Creating a dictionary that will allows keys and values as the objects
models = {"linear Regression" : LinearRegression(),
          "Decision Tree" : DecisionTreeRegressor(random_state = 42),
          "Random Forest" : RandomForestRegressor(n_estimators = 100, random_state = 42)}

#creating an empty dictionary to hold the results
results = {}

#creating the for loop to train the data and also do the predictions
for name, model in models.items():
    #using the fit() method to train the data
    model.fit(x_train, y_train)
    #making the predictions
    y_pred = model.predict(x_test)
    
    #measuring the average magnitude of the errors in the predictions
    mae = mean_absolute_error(y_test, y_pred)
    #penalising large errors more heavily than the ones in mae variable
    mse = mean_squared_error(y_test, y_pred)
    #checks how well the model explains the variance in the data
    r2 = r2_score(y_test, y_pred)
    
    #storing the results found 
    results[name] = {"Mean Absolute Error": mae, "Mean Squared Error"  : mse, "R2 Score" : r2}
    
#converting the results to a DataFrame
resultsData = pd.DataFrame(results).T
#outputting the results
print("-------------PERFORMANCE METRICS (MAE, MSE, R2) FOR EACH MODEL------------------")
print("------------------------------------------------------------------------------")
print(resultsData)
print("------------------------------------------------------------------------------")
    
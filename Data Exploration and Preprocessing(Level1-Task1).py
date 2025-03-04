import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#loading the dataset using pandas
data = pd.read_csv("C:/Users/KB.com/OneDrive/Pictures/Mabonono/Internship Tasks/cognify internship/Dataset .csv")

#outputing the first five rows of the dataset
print("------------------------------------------------------------------------")
print("-------------------------FIRST FIVE ROWS--------------------------------")
print("------------------------------------------------------------------------")
print(data)
print("------------------------------------------------------------------------")

#outputing the number of columns and rows
print("---------------------NUMBER OF COLUMNS AND ROWS-------------------------")
print("------------------------------------------------------------------------")
print("Number of rows: ", data.shape[0])
print("Number of columns: ", data.shape[1])
print("------------------------------------------------------------------------")

#checking for the missing values and outputting the columns after doing the process
missingValues = data.isnull()
print("-----------COLUMNS AFTER CHECKING FOR MISSING VALUES--------------------")
print("------------------------------------------------------------------------")
print(missingValues.sum())
print("------------------------------------------------------------------------")

#outputting columns ONLY with missing values
missingColumns = data.columns[data.isnull().sum() > 0]
print("------------------COLUMNS WITH MISSING VALUES---------------------------")
print("------------------------------------------------------------------------")
print(data[missingColumns].isnull().sum())
print("------------------------------------------------------------------------")

#handling the the column with missing values
for col in missingColumns:
    #checking if the data type of the column is an object
    if data[col].dtype == "object":
        #filling in the missing columns by grouping them according to the most common cities of around that/near the columns values 
        #(e.g. filling the missing cuisine value with the cuisine that of the resturant that is in the same city ) 
        data[col] = data.groupby("City")[col].transform(lambda x:
                                                        x.fillna(x.mode()[0]
                                                                 if not x.mode().empty
                                                                 else "Unknown"))
    else:
        #filling the numerical missing values with the median
        data[col] = data[col].fillna(data[col].median())
        
#verifying if there are still missing values or not
if data.isnull().sum().sum() == 0:
    #the output that will display if there are no missing values anymore
    print("ALL MISSING VALUES WERE HANDLED SUCCESSFULY!!!")
else:
    #if there is still missing values, then those missing values will be displayed 
    print(data.isnull().sum())
print("------------------------------------------------------------------------")

#checking the data types of each column in the datset and displaying them
dataTypes = data.dtypes
print("--------------------DATA TYPES OF EACH COLUMN---------------------------")
print("------------------------------------------------------------------------")
print(dataTypes)
print("------------------------------------------------------------------------")

#creating an empty dictionary that will hold all columns with incorrect data type
incorrectColumns = {}

#using a for loop to check for the expected data types
for column, expectedType in dataTypes.items():
    if column in data.columns:
        actualType = data[column].dtype
        if actualType != expectedType:
            incorrectColumns[column] = {'actual':actualType, "expected":expectedType}
            
if incorrectColumns:
    #outputting the columns that has all of the incorrect data types
    print("COLUMNS WITH INCORRECT DATA TYPES: ")
    for column, types in incorrectColumns.items():
        print(f"{column}: Expected {types['expected']}, Found {types['actual']}")
else:
    #outputting the message, showing that there are no columns with incorrect data types
    print("\nALL COLUMNS HAVE THE CORRECT DATA TYPE!!.")  
print("------------------------------------------------------------------------")


#visualizing the distribution of Aggregate rating to see if they are normally distributed or if they are clustered in certain ranges
plt.figure(figsize=(8, 5))
sns.histplot(data['Aggregate rating'], bins = 20, kde = True)
plt.title("Distribution of Aggregate Rating")
plt.xlabel("Aggregate Rating")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()

#outputting the statistical description of Aggregate rating to show the tendency and how spread the data is.
print("----------------SUMMARY STATISTICS FOR AGGREGATE RATING-----------------")
print("------------------------------------------------------------------------")
print(data['Aggregate rating'].describe())
print("------------------------------------------------------------------------")

#indentifying any class imbalances
#creating bins, labels and rating category so to rate the class imbalances 
bins = [0, 2, 4, 5]
labels = ['Low', 'Medium', 'High']
data['Rating Category'] = pd.cut(data['Aggregate rating'], bins = bins, labels = labels)

#outputting the class imbalances within the rating categories
rating_counts = data['Rating Category'].value_counts()
print("\n-------------------CLASS IMBALANCE IN RATING CATEGORIES-----------------")
print("------------------------------------------------------------------------")
print(rating_counts)
print("------------------------------------------------------------------------")

#visualizing the class imbalances within the categories
plt.figure(figsize = (10, 6))
sns.countplot(x = 'Rating Category', data = data)
plt.title("Class Distribution in Rating Categories")
plt.xlabel("Rating Category")
plt.ylabel("Count")
plt.grid(True)
plt.show()
import pandas as pd

#loading the dataset using pandas
data = pd.read_csv("C:/Users/KB.com/OneDrive/Pictures/Mabonono/Internship Tasks/cognify internship/Dataset .csv")

#outputing the first five rows of the dataset
print("------------------------------------------------------------------------")
print("-------------------------FIRST FIVE ROWS--------------------------------")
print("------------------------------------------------------------------------")
print(data)
print("------------------------------------------------------------------------")

#checking and outputting the statistical measures of the dataset using the describe() method
statisticalMeasures = data.describe()
print("-----------------SUMMARY STATISTICAL MEASURES---------------------------")
print("------------------------------------------------------------------------")
print(statisticalMeasures)
print("------------------------------------------------------------------------")

#exploring the distribution of Country Code
countryCodeCounts = data['Country Code'].value_counts()
print("---------------------COUNTRY CODE DISTRIBUTION--------------------------")
print("------------------------------------------------------------------------")
print(countryCodeCounts)
print("------------------------------------------------------------------------")

#exploring the distribution of City
cityCounts = data['City'].value_counts()
print("---------------------------CITY DISTRIBUTION----------------------------")
print("------------------------------------------------------------------------")
print(cityCounts)
print("------------------------------------------------------------------------")

#exploring the distribution of Cuisines
cusinesCounts = data['Cuisines'].value_counts()
print("-------------------------CUISINES DISTRIBUTION--------------------------")
print("------------------------------------------------------------------------")
print(cusinesCounts)
print("------------------------------------------------------------------------")

#outputting the number of unique categories in each categorical column
print("---------NUMBER OF UNIQUE CATEGORIES IN EACH CATEGORICAL COLUMN---------")
print("------------------------------------------------------------------------")
print("Unique Categories in Country code: ", data['Country Code'].nunique())
print("Unique Categories in City: ", data['City'].nunique())
print("Unique Categories in Cuisines: ", data['Cuisines'].nunique())
print("------------------------------------------------------------------------")

#outputtiing top 5 cuisines with the highest number of resturants
topCuisines = cusinesCounts.head(5)
print("---------TOP CUISINES WITH THE HIGHEST NUMBER OF RESTURANTS-------------")
print("------------------------------------------------------------------------")
print(topCuisines)
print("------------------------------------------------------------------------")

#outputtiing top 5 cities with the highest number of resturants
print("---------TOP CITIES WITH THE HIGHEST NUMBER OF RESTURANTS---------------")
topCity = cityCounts.head(5)
print("------------------------------------------------------------------------")
print(topCity)
print("------------------------------------------------------------------------")
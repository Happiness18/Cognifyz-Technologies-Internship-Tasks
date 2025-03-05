import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#loading the dataset using pandas
data = pd.read_csv("C:/Users/KB.com/OneDrive/Pictures/Mabonono/Internship Tasks/cognify internship/Dataset .csv")

#outputting the first five rows of the dataset
print("--------------------------------------------------------------------------")
print("----------------------------FIRST FIVE ROWS-------------------------------")
print("--------------------------------------------------------------------------")
print(data.head())
print("--------------------------------------------------------------------------")

#dropping Cuisines missing values column
data = data.dropna(subset = ['Cuisines'])

#splitting multiple Cuisines into seperate list items
data['Cuisines'] = data['Cuisines'].str.split(', ')
#expands the list into seperate rows
data = data.explode('Cuisines')

#grouping the data by Cuisines and calculating the average of each Aggregate rating for Cuisines
cuisineRatings = data.groupby('Cuisines')['Aggregate rating'].mean().reset_index()
#sorting Cuisines based on average rating in descending order
cuisineRatings = cuisineRatings.sort_values(by = 'Aggregate rating', ascending = False)

#grouping the data by Cuisines and calculating the sum of Votes for Cuisines
cuisineVotes = data.groupby('Cuisines')['Votes'].sum().reset_index()
#sorting Cuisines based on total votes in descending order
cuisineVotes = cuisineVotes.sort_values(by = 'Votes', ascending = False)

#assigning the top ten cuisine ratings to a variable 
topRatedCuisines = cuisineRatings.head(10)
#assigning the top ten cuisine votes to a variable 
mostPopularCuisines = cuisineVotes.head(10)

#plotting the top 10 highest rated cuisines
plt.figure(figsize = (12, 5))
sns.barplot(x = topRatedCuisines['Cuisines'], y = topRatedCuisines['Aggregate rating'], hue = topRatedCuisines['Cuisines'], palette = "viridis", legend = False)
plt.title("Top 10 Cuisines with Highest Average Ratings")
plt.xlabel("Cuisines")
plt.ylabel("Average Rating")
plt.xticks(rotation = 45, ha = 'right')
plt.show()

#plotting the top 10 most popular cuisines
plt.figure(figsize = (12, 5))
sns.barplot(x = mostPopularCuisines['Cuisines'], y = mostPopularCuisines['Votes'], hue = mostPopularCuisines['Cuisines'],palette = "magma", legend = False)
plt.title("Top 10 Most Popular Cuisines Based on Votes")
plt.xlabel("Cuisine Type")
plt.ylabel("Total Votes")
plt.xticks(rotation = 45, ha = 'right')
plt.show()

#printing the results
print("---------------TOP 10 CUISINES WITH HIGHEST AVERAGE RATINGS---------------")
print("--------------------------------------------------------------------------")
print(topRatedCuisines)
print("--------------------------------------------------------------------------")
print("--------------TOP 10 MOST POPULAR CUISINES BASED ON VOTES-----------------")
print("--------------------------------------------------------------------------")
print(mostPopularCuisines)
print("--------------------------------------------------------------------------")
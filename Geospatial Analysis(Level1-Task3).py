import pandas as pd
import folium
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

#calculating and assigning the average of longitute and latitude to the variable mapLocation
mapLocation = [data['Latitude'].mean(), data['Longitude'].mean()]
#creating the base map of longitude aand latitude
restaurantMap = folium.Map(location = mapLocation, zoom_start=3)

#creating a for loop that will iterate through the index of each row of the dataset
for index, row in data.iterrows():
    #creating a circle marker for each restaurant
    folium.CircleMarker(
        #assigning the locations 
        location = [row['Latitude'], row['Longitude']],
                    radius = 3,
                    color = "blue",
                    fill = True,
                    fill_color = "blue",
                    fill_opacity = 0.6,
                    ).add_to(restaurantMap) #adding the created circle to the restaurantMap
 
    #saving the interactive map as an HTML file
restaurantMap.save("Restaurant Map.html")
#outputting the following message after the map being saved
print("Interactive map saved as Restaurant Map.html. The file is available in the browser for viewing the map.")
print("--------------------------------------------------------------------------")

#counting number of restaurants in each city
cityCounts = data['City'].value_counts().head(10)
#counting number of restaurants in each country
countryCodeCounts = data['Country Code'].value_counts().head(10)

#plotting restaurant distribution by city
plt.figure(figsize = (12, 5))
cityCounts.plot(kind = "bar", color = "blue")
plt.title("Top 10 Cities with the Most Restaurants")
plt.xlabel("City")
plt.ylabel("Number of Restaurants")
plt.xticks(rotation = 45)
plt.show()

#plotting restaurant distribution by coutry
plt.figure(figsize = (12, 5))
countryCodeCounts.plot(kind = "bar", color = "green")
plt.title("Top 10 Countries with the Most Restaurants")
plt.xlabel("Country Code")
plt.ylabel("Number of Restaurants")
plt.xticks(rotation = 45)
plt.show()

#computing the correlation matrix
correlationMatrix = data[["Latitude", "Longitude", "Aggregate rating"]].corr()

#plotting a heatmap to show the correlation between locations and rating
plt.figure(figsize = (8, 5))
sns.heatmap(correlationMatrix, annot = True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Between Location and Ratings")
plt.show()

#computing the correlation between Latitude and Aggregate rating
latitudeCorrelation = data["Latitude"].corr(data["Aggregate rating"])
#computing the correlation between Longitude and Aggregate rating
longitudeCorrelation = data["Longitude"].corr(data["Aggregate rating"])

print("---CORRELATION BETWEEN (LATITUDE AND AGGREGATE RATING) AND (LONGITUDE AND AGGREGATE RATING)---")
print("----------------------------------------------------------------------------------------------")
#outputting the correlation between Latitude and Aggregate rating
print(f"Latitude vs TRating Correlation: {latitudeCorrelation:.2f}")
#outputting the correlation between Longitude and Aggregate rating
print(f"Longitude vs TRating Correlation: {longitudeCorrelation:.2f}")
print("----------------------------------------------------------------------------------------------")

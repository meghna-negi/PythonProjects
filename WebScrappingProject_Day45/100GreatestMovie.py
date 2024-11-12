from bs4 import BeautifulSoup
import requests

#Retrieving the data from the empire ranking page
response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
whole_webpage = response.text
movies_list = []

#Creating soup object for web scrapping
Soup = BeautifulSoup(whole_webpage,"html.parser")

#Getting list of all anchor tags
anchor_tag = Soup.find_all(name="a")

#Iterating over anchors and choosing the anchor which have data-test attribute
#Append such tag's data-test attributes value to the movies list
for anchor in anchor_tag:
    movie_tag = anchor.get("data-test")
    if(movie_tag is not None and movie_tag != "logo-link"):
        movies_list.append(movie_tag)

#Reversing the obtained list to get ranking from 1-100
top_100 = movies_list[::-1]

#Writing the movie name and it's rank in a txt file
with open("movielist.txt",mode="w") as file:
    index = 1
    for movie in top_100:
        print(movie)
        file.write(f"{index}. {movie}\n")
        index += 1
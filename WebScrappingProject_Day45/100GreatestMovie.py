from bs4 import BeautifulSoup
import requests

#Retrieving the data from the empire ranking page
response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
whole_webpage = response.text
movies_list = []

#Creating soup object for web scrapping
Soup = BeautifulSoup(whole_webpage,"html.parser")

#finding movie names and rank
header_tags = Soup.findAll(name = "h3", class_ = "title")
for movie in header_tags[::-1]:
    movies_list.append(movie.getText())

#Writing the movie name and it's rank in a txt file
with open("movielist.txt",mode="w", encoding="utf-8") as file:
    for movie in movies_list:
        file.write(f'{movie}\n')

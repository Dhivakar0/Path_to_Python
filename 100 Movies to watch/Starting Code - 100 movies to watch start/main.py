import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url=URL)
contents = response.text

soup = BeautifulSoup(contents,"html.parser")

movie_titles = [article.getText() for article in  soup.find_all('h3',class_="title")]
movie_titles.reverse()

with open("movies.txt","a",encoding="utf-8") as file:
    for movie in movie_titles:
        file.write(movie + "\n")

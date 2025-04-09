from bs4 import BeautifulSoup
import requests

travel = input("Which year do you want to travel to? Type the data in this format YYYY-MM-DD: ")

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

# from bs4 import BeautifulSoup
# import requests
#
# # https://www.billboard.com/charts/hot-100/2000-08-12
#
# travel = input("Which year do you want to travel to? Type the data in this format YYYY-MM-DD: ")
#
# header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

def func(x, y=[]):
    y.append(x)
    return y


print(func(1))
print(func(2))
print(func(3, []))
print(func(4))

import requests
from bs4 import BeautifulSoup

response = requests.get("http://appbrewery.github.io/news.ycombinator.com/",verify=False)
contents = response.text

soup = BeautifulSoup(contents,"html.parser")
article_tag = soup.find_all('a',class_="storylink")
article_texts = []
article_links = []

for article in article_tag:
    text = article.getText()
    article_texts.append(text)
    link = article.get("href")
    article_links.append(link)
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name='span',class_='score')]

print(article_texts)
print(article_links)
print(article_upvotes)

max_upvotes = max(article_upvotes)

max_upvotes_index = article_upvotes.index(max_upvotes)

print(article_texts[max_upvotes_index])
print(article_links[max_upvotes_index])
print(max_upvotes)


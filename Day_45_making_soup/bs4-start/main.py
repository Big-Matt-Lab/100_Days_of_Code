import requests
from bs4 import BeautifulSoup

URL = "https://news.ycombinator.com/news"

# Get raw data from website
response = requests.get(URL, timeout=5)
response.raise_for_status()
data = response.text

# Make soup
soup = BeautifulSoup(data, "html.parser")
title_spans = soup.find_all(name="span", class_="titleline")
articles = [span.find("a") for span in title_spans]

article_texts = [article.getText() for article in articles]
article_links = [article.get("href") for article in articles]

article_upvotes = [
    int(score.getText().split()[0])
    for score in soup.find_all(name="span", class_="score")
]

# # Combine the lists and find the tuple with the highest upvote
# max_vote, max_title, max_link = max(zip(article_upvotes, article_texts, article_links))
#
# print(f"Highest Score: {max_vote}")
# print(f"Title: {max_title}")
# print(f"Link: {max_link}")

# Find the index of the highest integer
max_index = article_upvotes.index(max(article_upvotes))

# Retrieve the matching items
max_title = article_texts[max_index]
max_link = article_links[max_index]
max_vote = article_upvotes[max_index]

print(f"Highest Score: {max_vote}")
print(f"Title: {max_title}")
print(f"Link: {max_link}")

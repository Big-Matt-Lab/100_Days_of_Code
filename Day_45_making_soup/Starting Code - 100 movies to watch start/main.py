"""Udemy - 100 Days of Code:
The Complete Python Pro Bootcamp

*** 100 Movies to Watch Scraper ***
This script is designed to scrape a curated list of the top 100 movies of all time
from the Empire Online magazine website (using an archived version via Wayback Machine).
It extracts movie titles, processes them to separate the rank from the title,
and then prints the list in ascending order.

Python Concepts Highlighted:
- `requests` module for making HTTP GET requests to fetch web page content (`requests.get()`).
- `BeautifulSoup` for HTML parsing and web scraping (`BeautifulSoup`, `soup.find_all()`, `getText()`).
- List comprehensions for concisely extracting data from HTML elements (`movies = [...]`).
- List manipulation methods for organizing data (`list.append()`, `list.reverse()`).
- String methods for data cleaning and parsing (`str.replace()`, `str.split()`, `str.strip()`).
- F-strings for formatted output to the console (`print(f"...")`).
- Error handling for HTTP requests (`response.raise_for_status()`).
"""

import requests
from bs4 import BeautifulSoup

# URL (str): The web address of the archived Empire Online page listing the top 100 movies.
# This global constant specifies the target for our web scraping request.
URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Make an HTTP GET request to the specified URL to fetch the raw HTML content.
# A `timeout` of 5 seconds is set to prevent the program from hanging indefinitely
# if the server does not respond promptly.
response = requests.get(URL, timeout=5)
# Raise an `HTTPError` for bad responses (4xx or 5xx status codes), ensuring
# that the program stops and reports an error if the page cannot be fetched successfully.
response.raise_for_status()
# Extract the raw textual content (HTML) from the HTTP response.
data = response.text

# Initialize a `BeautifulSoup` object to parse the fetched HTML content.
# The "html.parser" argument specifies the parser to use for HTML documents.
soup = BeautifulSoup(data, "html.parser")
# Find all `h3` tags in the HTML document that have the `class` attribute set to "title".
# These tags are identified as containing the movie titles on this specific webpage.
all_movies = soup.find_all(name="h3", class_="title")

# Use a list comprehension to extract the text content from each `h3` tag found.
# This results in a list where each element is a string like "100) The Godfather" or "99) Movie Title: Subtitle".
movies = [film.getText() for film in all_movies]
movies.reverse()

# Iterate through each raw movie string extracted from the HTML
# and write the list to a new file (or amend an existing file)
with open("movies.txt", mode="w") as file:
    for movie in movies:
        print(f"{movie}")
        file.write(f"{movie}\n")

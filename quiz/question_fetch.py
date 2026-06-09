"""Udemy - 100 Days of Code:
The Complete Python Pro Bootcamp

*** Question Fetcher Module ***
This module provides the `QuestionFetcher` class, responsible for fetching
quiz questions from the Open Trivia Database API and cleaning the data
into a usable format.

Python Concepts Highlighted:
- `import requests` for making HTTP requests to external APIs.
- `import html` for unescaping HTML entities in fetched data.
- Class definition and `__init__` constructor for object initialization.
- Instance attributes (`self.category_id`, `self.base_url`).
- String formatting (f-strings) for dynamic URL construction.
- `requests.get()` for sending GET requests.
- `response.raise_for_status()` for error handling HTTP responses.
- `response.json()` for parsing JSON API responses.
- Dictionary access (`data['results']`) for navigating JSON structure.
- List iteration (`for` loop) and `list.append()` for data transformation.
- Dictionary creation for structuring cleaned question data.
- `html.unescape()` for cleaning HTML entities from question text.
"""

# Python concept: Importing the `requests` library for making HTTP requests.
import requests
# Python concept: Importing the `html` module for handling HTML entities.
import html

class QuestionFetcher:
    """
    Fetches quiz questions from the Open Trivia Database API and cleans them.

    Attributes:
        category_id (int, optional): The ID of the desired question category.
                                     If `None`, questions from any category are fetched.
        base_url (str): The base URL for the Open Trivia Database API.
    """

    def __init__(self, category_id=None):
        """
        Initializes the QuestionFetcher with an optional category ID.

        Args:
            category_id (int, optional): The ID of the question category to fetch.
                                         Defaults to `None` for any category.
        """
        # Python concept: Instance attribute `self.category_id` to store the category configuration.
        self.category_id = category_id
        # Python concept: Instance attribute `self.base_url` storing the API endpoint.
        # This is a constant part of the URL for fetching 50 easy boolean questions.
        self.base_url = "https://opentdb.com/api.php?amount=10&difficulty=easy&type=boolean"

    def fetch_and_clean_data(self):
        """
        Fetches data from the Open Trivia Database API and returns a list of
        formatted dictionaries, each containing a question's text and answer.

        Returns:
            list[dict]: A list of dictionaries, where each dictionary has
                        "text" (str) and "answer" (str) keys.
        """
        # Python concept: Building a dynamic URL using f-strings.
        url = self.base_url
        # Python concept: Conditional logic to append category parameter if `category_id` is provided.
        if self.category_id:
            url += f"&category={self.category_id}"
            
        # Python concept: `requests.get()` to send an HTTP GET request to the API.
        response = requests.get(url)
        # Python concept: `response.raise_for_status()` to check for HTTP errors (e.g., 404, 500).
        response.raise_for_status()
        # Python concept: `response.json()` to parse the JSON response body into a Python dictionary.
        data = response.json()
        
        # Python concept: Dictionary access to extract the list of question results.
        results = data['results']
        # Python concept: `cleaned_questions` is a list that will store processed question dictionaries.
        cleaned_questions = []
        # Python concept: `for` loop to iterate through each raw question item.
        for item in results:
            # Python concept: `html.unescape()` to convert HTML entities (like `&quot;`) into readable characters.
            # Python concept: Dictionary creation to structure the cleaned question data.
            cleaned_questions.append({
                "text": html.unescape(item["question"]),
                "answer": item["correct_answer"]
            })
            
        return cleaned_questions
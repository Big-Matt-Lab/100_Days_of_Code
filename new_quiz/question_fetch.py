"""Udemy - 100 Days of Code:
The Complete Python Pro Bootcamp

*** Question Fetcher Module ***
This module contains the `QuestionFetcher` helper class which handles pulling raw
boolean trivia question data from the Open Trivia Database (OTDB) API over HTTP.

Python Concepts Highlighted:
- `requests.get()` for making API network requests with custom dynamic payload parameters.
- `html.unescape()` to safely parse and convert nested HTML entities in responses.
- `raise_for_status()` for basic standard HTTP error detection and response checking.
"""

import html

import requests


class QuestionFetcher:
    """Fetches quiz questions from the Open Trivia Database API and cleans them.

    Attributes:
        category_id (int, optional): The ID of the desired question category.
                                     If `None`, questions from any category are fetched.
        url (str): The base URL endpoint for the Open Trivia Database API.
    """

    def __init__(self, category=None):
        """Initializes the QuestionFetcher with an optional category ID.

        Args:
            category (int, optional): The ID of the question category to fetch.
                                      Defaults to `None` for any category.
        """
        # Python concept: Instance attributes store configuration state for future calls.
        self.category_id = category
        self.url = "https://opentdb.com/api.php"

    def fetch_and_clean_data(self):
        """Fetches data from the Open Trivia Database API and returns a list of

        formatted dictionaries, each containing a question's text and answer.

        Returns:
            list[dict]: A list of dictionaries, where each dictionary has
                        "text" (str) and "answer" (str) keys.
        """
        parameters = {
            "amount": 10,
            "difficulty": "easy",
            "type": "boolean",
        }

        # Python concept: Conditionals to append optional API parameter configurations.
        if self.category_id != 0:
            parameters["category"] = self.category_id

        # Python concept: `requests.get()` handles initiating network connections and payloads.
        response = requests.get(self.url, params=parameters, timeout=5)
        # Python concept: Checking the HTTP response code to detect networking errors.
        response.raise_for_status()
        # Python concept: Parsing the returned binary payload format into standard Python JSON/dict.
        data = response.json()

        results = data["results"]
        cleaned_questions = []
        for item in results:
            # Python concept: Decoding and unescaping standard encoded HTML symbols like `"`.
            cleaned_questions.append({
                "text": html.unescape(item["question"]),
                "answer": item["correct_answer"]
            })

        return cleaned_questions

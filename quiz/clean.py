
from question_model import Question
import requests

def fetch_data():
    url = "https://opentdb.com/api.php?amount=50&category=9&type=boolean"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def prep_data(data):
    results = data['results']
    new_question_list = []
    for item in results:
        new_question_list.append({
            "question": item["question"],
            "correct_answer": item["correct_answer"]
        })
    return new_question_list

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

def write_data(data_to_write):
    with open('data.py', 'w') as f:
        f.write(f"question_data = {data_to_write}")

json_data = fetch_data()
cleaned_data = prep_data(json_data)
write_data(cleaned_data)

import requests
import json

api_url = "https://opentdb.com/api.php?amount=3&category=11&difficulty=medium"

parameters = {
    "category": "Entertainment: Film"
}

response = requests.get(api_url)

category_url = "https://opentdb.com/api_category.php"
categories = requests.get(category_url)
categories.json()

api_url = "https://opentdb.com/api.php?amount=3&category=11&difficulty=medium"
response = requests.get(api_url)
question = response.json()

def jprint(query):
    text = json.dumps(question, sort_keys=True, indent=4)
    print(text)

jprint(response.json())

answers = []

for ans in answers:
    choices = ans["incorrect answers", "correct_answer"]
    answers.append(choices)

print(answers)
import requests

print("Let's get some trivia questions!\n")

amount = input('Number of Questions (1-50): ')

print(
    '\nCategories: \nany: Any Category\n9: General Knowledge\n10: Entertainment: Books\n11: Entertainment: Film\n12: Entertainment: Music\n13: Entertainment: Musicals & Theatres\n14: Entertainment: Television\n15: Entertainment: Video Games\n16: Entertainment: Board Games\n17: Science & Nature\n18: Science: Computers\n19: Science: Mathematics\n20: Mythology\n21: Sports\n22: Geography\n23: History\n24: Politics\n25: Art\n26: Celebrities\n27: Animals\n28: Vehicles\n29: Entertainment: Comics\n30: Science: Gadgets\n31: Entertainment: Japanese Anime & Manga\n32: Entertainment: Cartoon & Animations')
trivia_category = input('\nCategory: \n')
category = ''
if trivia_category != 'any':
    category = f'&category={trivia_category}'

trivia_difficulty = input('\nSelect Difficulty (any/easy/medium/hard): ')
difficulty = ''
if trivia_difficulty != 'any':
    difficulty = f'&difficulty={trivia_difficulty}'

print('\nTypes: \nany: Any Type\nmultiple: Multiple Choice\nboolean: True / False')
trivia_type = input('\nType: ')
type_ = ''
if trivia_type != 'any':
    type_ = f'&type={trivia_type}'

# # Keep the default encoding or it messes up out info retrieval:
# print('\nEncodings: \ndefault: Default Encoding\nurlLegacy: Legacy URL Encoding\nurl3986: URL Encoding (RFC 3986)\nbase64: Base64 Encoding')
# encoding = input('\nEncoding: ')

# url = 'https://opentdb.com/api.php?amount=10&category=17&difficulty=hard&type=multiple'
# url = f'https://opentdb.com/api.php?amount={amount}&category={category}&difficulty={difficulty}&type={type_}&encode={encoding}'
url = f'https://opentdb.com/api.php?amount={amount}{category}{difficulty}{type_}’
# print(url)

response = requests.get(url)

list_trivias = response.json()
# print(list_trivias)

results = list_trivias['results']
# print(results)
print('\n')

# Let's write the questions on the screen and in a new file:
with open('trivia.txt', 'w') as trivia_file:
    #     breakpoint()

    trivia_file.write(f'Number of Questions (1-50): {amount}\n')
    #     trivia_file.write(f'Category: {category}\n')
    #     trivia_file.write(f'Difficulty: {difficulty}\n')
    #     trivia_file.write(f'Type: {type_}\n')
    trivia_file.write('\n')

    for index, result in enumerate(results):
        question = result['question']
        print(question)
        trivia_file.write(f'Question {index + 1}: {question}\n')

        correct = result['correct_answer']
        print(correct)
        trivia_file.write(f'O {correct}\n')

        incorrect = result['incorrect_answers']
        for incorrect_answer in incorrect:
            print(incorrect_answer)
            trivia_file.write(f'X {incorrect_answer}\n')

        print('\n')
        trivia_file.write('\n')
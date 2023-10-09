import json
import random
# +1
question_json: str = input("Which subject? ")

questions: dict[str, str] = json.load(open(f"{question_json.upper()}/{question_json.lower()}.json", "r"))
question_list = list(questions.keys())
random.shuffle(question_list)
score = 0

wrong_questions = []

for question in question_list:
    answer = input(f"{question}: ")
    if answer.lower() == questions[question].lower():
        print("Correct!")
        score += 1
    else:
        print("Incorrect, the correct answer is: " + questions[question])
        wrong_questions.append(question)
    print("\n")

print(f"Your score is: {score}/{len(questions)}\n")
print("Questions you got wrong: ")

for question in wrong_questions:
    print(f"""{question}: 
          Correct Answer: {questions[question]}""")

input("Press enter to exit...")
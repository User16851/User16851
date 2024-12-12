import random

print("This is a math quiz. Give your answer to 2 decimal places.")

no_of_question = int(input("Enter the number of questions you want to answer: "))
score = 0

for x in range(no_of_question):
    number_1 = random.randint(0, 10)
    number_2 = random.randint(0, 10)
    symbols = ["+", "-", "*", "/"]
    symbol = symbols[random.randint(0, 3)]
    answer = float(input(f"Question {x+1}: {number_1} {symbol} {number_2} = "))
    if symbol == "+":
        correct_answer = round(number_1 + number_2,2)
    if symbol == "-":
        correct_answer = round(number_1 - number_2,2)
    if symbol == "*":
        correct_answer = round(number_1 * number_2,2)
    if symbol == "/":
        correct_answer = round(number_1 / number_2,2)
    if answer == correct_answer:
        score += 1
        print(f"Correct! Score = {score}")
    elif answer != correct_answer:
        score -= 1
        print(f"Incorrect! Score = {score}")

print(f"Final score = {score} / {no_of_question}")

import random

print("This is a 4-digit number guessing game. The digits in the number do not repeat.")
number = str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9))
number_of_guesses = 0
while True:
    guessed_number = str(input("Enter your number: "))
    number_of_guesses += 1

    def make_number_unqiue(number):
        total_digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        digits_used = []
        for x in range(4):
            digits_used.append(number[x])
        unqiue_digits_used = list(set(digits_used))
        for y in range(len(unqiue_digits_used)):
            total_digits.remove(unqiue_digits_used[y])
        for z in range(4 - len(unqiue_digits_used)):
            unqiue_digits_used.append(total_digits[random.randint(0, len(total_digits))])
        number = "".join(unqiue_digits_used)

        return number

    number = make_number_unqiue(number)

    def count_correct_digits(number, guessed_number):
        total_digit_correct = 0
        for x in range(4):
            digit_count = number.count(number[x:x+1])
            guessed_digit_count = guessed_number.count(number[x:x+1])
            correct_count = min(digit_count, guessed_digit_count)
            total_digit_correct += correct_count

        return min(total_digit_correct, 4)

    def count_correct_position(number, guessed_number):
        total_position_correct = 0
        for x in range(4):
            if number[x] == guessed_number[x]:
                total_position_correct += 1
        return total_position_correct

    total_position_correct = count_correct_position(number, guessed_number)
    total_digit_correct = count_correct_digits(number, guessed_number)

    print(f"You got {total_digit_correct} digits correct! {total_position_correct} of them are in the correct position!")
    if total_digit_correct == total_position_correct == 4:
        print(f"You have solved the unknown number in {number_of_guesses} guesses!")
        break
import random
from xml.dom import WrongDocumentErr

bag_of_words = ['Edureka',"python", "machinelearning", "looping", "whileloop", "devops", "forloop", "deeplearning", "oops", "condition", "preprocessing", "modelling", "algorithms", "parameters", "control", "exception", "nomalization"]
word = random.choice(bag_of_words)
word_list = sorted(list(word))
guess = []
wrong_guess = ""
counter = 0

name = input("What is your name?: ")
print(f"Hello, {name}! Let's play some hagnman!")
print("So what's your first guess?")

for i in word:
    print("_", end = " ")
print("\n")

while word_list != guess:
    letter = input("Guess a letter: ")
    if letter in word:
        guess.append(letter)
        guess = sorted(guess)
        for i in word:
            if i in guess:
                print(i, end = " ")
            else:
                print("_", end = " ")
        print("\n")
    else:
        wrong_guess += letter + " "
        print(f"Sorry but '{letter.lower()}' isn't in the word!")
        print(f'You have {5 - counter} more chances :(')
        print("Try again!")
        print(f'Your previous wrong guesses are: {wrong_guess}')
        counter += 1
        if counter == 5:
            print("I'm sorry but you've lost :(")
            print(f'The word you were looking for was: {word.upper()}')
            break
    word_list = sorted(list(dict.fromkeys(word_list))) # remove duplicates
    guess = sorted(list(dict.fromkeys(guess))) # remove duplicates
    if word_list == guess:
        print("Congratz!!! You've won!!!")
        print(f'The word you were looking for was: {word.upper()}')
        break
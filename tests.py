import random


def initialization():
    bag_of_words = ['Edureka',"python", "machinelearning", "looping", "whileloop", "devops", "forloop", "deeplearning", "oops", "condition", "preprocessing", "modelling", "algorithms", "parameters", "control", "exception", "nomalization"]
    word = random.choice(bag_of_words).lower() # ver la manera de pasarla en mayúscula
    word_list = sorted(list(word.lower())) # aquí sale sobrando el ower pero no me afecta
    print("So, what's your first guess?")
    for i in word:
        print("_", end = " ")
    print("\n")
    return word, word_list

def game(name, word, word_list):
    print(f"Hello, {name}! Let's play hagnman!")
    guess = []
    wrong_guess = ""
    counter = 0
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
            for i in word:
                if i in guess:
                    print(i, end = " ")
                else:
                    print("_", end = " ")
            print("\n")
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

if __name__ == '__main__':

    print("Hello! This is the game of HANGMAN")
    name = "Orlando" # input("What is your name?: ")
    play = True
    again = False
    
    while play:
        word, word_list = initialization()
        game(name, word, word_list)
        while again == False:
            asking = input("Do you want to play again (Y/N)?: ")
            if asking.lower() == "n":
                print(f"Great! See you later {name}!")
                play = False
                break
            elif asking.lower() == "y":
                print(f"Let's play again then {name}!")
                again == True
                break
            else:
                print(f"That's not a valid answer {name}! \nPlease tell me!")

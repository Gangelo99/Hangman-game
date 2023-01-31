import random
import os

word_list = ["hello", "football", "road", "apple", "linux"]
chosen_word = random.choice(word_list) #This is the chosen word for the game
word_underscore = '_' * len(chosen_word) #This is the chosen word replaced with underscore
life = 5

def check_char(letter: str) -> bool:
    global chosen_word
    global word_underscore
    global life
    letter_found = False
    for i in range(len(chosen_word)):
        if(letter == chosen_word[i]):
            print("Letter guess!")
            letter_found = True
            word_underscore = word_underscore[:i] + letter + word_underscore[i + 1:] #Replace the 11
        
    if letter_found:
        return True
    
    print("\nLetter was not found :(")
    life -= 1
    return False

def check_goal() -> bool:
    if word_underscore.find('_') == -1:
        print("\nYou have found the word!\n")
        return True
    
    return False

def check_life() -> bool:
    return ((True, False) [life == False])

while not check_goal() and check_life():
    os.system('cls')
    print(word_underscore)
    print(f"\n❤  YOU HAVE: {life} life(s) ❤")
    guess = input("Guess a letter: ").lower()
    check_char(guess)
    print("\n-> " + word_underscore)
    os.system('pause')
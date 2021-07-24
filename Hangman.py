print("Welcome to Hangman :)")
player_word = input("Player 1 Enter a word: ")
# force lower case
word = player_word.lower()
# variable declaration
word_length = len(word)
guessed_word = "*"*word_length
lives = 7
letter_bin = []
# loop
print("Let's Play!")
while not lives == 0 and not guessed_word == word:
    print("Word Length = " + str(word_length))
    print("Lives left = " + str(lives))
    print(guessed_word)
    print(letter_bin)
    # input validation
    valid = False
    while not valid:
        letter = input("Player 2, enter letter:  ").lower()
        valid = True
        if not letter.isalpha():
            print("Error: Input is not a letter")
            valid = False
        if not len(letter) == 1:
            print("Error: Please enter a single letter")
            valid = False
        if letter in letter_bin or letter in guessed_word:
            print("Error: Please enter a new letter")
            valid = False
        # if not valid:
        #     letter = input("Input invalid. Try again:  ")
    letter = letter
    print() 
    if letter in word:
        print("Correct!")
        for count, l in enumerate(word):
            if letter == l:
                guessed_word = guessed_word[:count] + letter + guessed_word[count+1:]
    else:
        print("Try again! :(")
        lives -= 1
        letter_bin.append(letter)
if lives == 0:
    print("Sorry! you've lost")
else:
    print("You win!")
print("The word was " + player_word)

input("press enter to exit")
# 
#Improvements:  Player 1/Player 2 Turns (best of 5?) Homework!!!              
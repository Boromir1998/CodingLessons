print("Welcome to Hangman :)")
import getpass

Player = 2
Guesser = 1
Score=[]
Score.append(0)
Score.append(0)
Round = 0
while Score[0] < 3 and Score[1] < 3:
    # Switch Players
    # could elseif
    if Player == 1:
      Player = 2
    else:
      Player = 1
    Guesser = Player%2 + 1 #mod
    Round = Round + 1
    print ("Round " + str(Round))
    #old line: player_word = input("Player " + str(Player) + " Enter a word: ")
    print("Player " + str(Player) + " Enter a word:")
    player_word = getpass.getpass(prompt="-->")
    # force lower case
    word = player_word.lower()
    # variable declaration
    word_length = len(word)
    guessed_word = "*"*word_length
    lives = 7
    letter_bin = []
    # loop
    print()
    print("Let's Play!")
    while not lives == 0 and not guessed_word == word:
        print("Word Length = " + str(word_length))
        print("Lives left = " + str(lives))
        print(guessed_word)
        print("Used Letters" +str(letter_bin))
        print()
        # input validation
        valid = False
        while not valid:
            letter = input("Player " + str(Guesser) + ", enter letter:  ").lower()
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
        print("Sorry! Player " + str(Guesser) + " lost")
        Score[Player-1] +=1   
    else:
        print("Player " + str(Guesser) + " wins!")
        Score[Guesser-1] +=1
    print()
    print("The word was " + player_word)
    print("Player 1: " + str(Score[0])+ "; Player 2: "+ str(Score[1]))
    print()

input("press enter to exit")
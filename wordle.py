import random

letters = [ #creates a 2d list, where the first index choice is the letter, while the second index choice is the first, second, third, or fourth line of the ascii letter
        ["    db    ", "   dPYb   ", "  dPwwYb  ", " dP    Yb "], #a
        ["  888b.   ", "  8wwwP   ", "  8   b   ", "  888P'   "], #b
        ["  .d88b   ", "  8P      ", "  8b      ", "  `Y88P   "], #c
        ["  888b.   ", "  8   8   ", "  8   8   ", "  888P'   "], #d
        ["   8888   ", "   8www   ", "   8      ", "   8888   "], #e
        ["   8888   ", "   8www   ", "   8      ", "   8      "], #f
        ["  .d88b   ", "  8P www  ", "  8b  d8  ", "  `Y88P'  "], #g
        ["  8   8   ", "  8www8   ", "  8   8   ", "  8   8   "], #h
        ["   888    ", "    8     ", "    8     ", "   888    "], #i
        ["   8888   ", "     8    ", "  w  8    ", "  `Yw     "], #j
        ["  8  dP   ", "  8wdP    ", "  88Yb    ", "  8  Yb   "], #k
        ["   8      ", "   8      ", "   8      ", "   8888   "], #l
        [" 8b   d8  ", " 8YbmdP8  ", " 8  '  8  ", " 8     8  "], #m
        ["  8b  8   ", "  8Ybm8   ", "  8  '8   ", "  8   8   "], #n
        ["  .d88b.  ", "  8P  Y8  ", "  8P  Y8  ", "  `Y88P'  "], #o
        ["  888b.   ", "  8  .8   ", "  8wwP'   ", "  8       "], #p
        ["  .d88b.  ", "  8P  Y8  ", "  8b wd8  ", "  `Y88Pw  "], #q
        ["  888b.   ", "  8  .8   ", "  8wwK'   ", "  8  Yb   "], #r
        ["  .d88b.  ", "  YPwww.  ", "      d8  ", "  `Y88P'  "], #s
        ["  88888   ", "    8     ", "    8     ", "    8     "], #t
        ["  8    8  ", "  8    8  ", "  8b..d8  ", "  `Y88P'  "], #u
        [" Yb    dP ", "  Yb  dP  ", "   YbdP   ", "    YP    "], #v
        ["Yb      dP", " Yb db dP ", " YbdPYbdP ", "  YP  YP  "], #w
        ["  Yb  dP  ", "   YbdP   ", "   dPYb   ", "  dP  Yb  "], #x
        ["  Yb  dP  ", "   YbdP   ", "    YP    ", "    88    "], #y
        ["  8888P   ", "    dP    ", "   dP     ", "  d8888   "]] #z

line_divider = "+----------+----------+----------+----------+----------+----------+"
char_divider = "|          |          |          |          |          |          |"

thisdict = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7, "i": 8, "j": 9, "k": 10, "l": 11, "m": 12, "n": 13,
            "o": 14, "p": 15, "q": 16, "r": 17, "s": 18, "t": 19, "u": 20, "v": 21, "w": 22, "x": 23, "y": 24, "z": 25}
def wordle():
    print("\nWelcome to 6-letter Wordle!")
    print("You are allowed 6 guesses of 6-letter words.")
    print("\033[31m" + "Red" + "\x1b[0m", "letters are correct letters, but in the wrong spot.")
    print("\033[35m" + "Purple" + "\x1b[0m", "letters are correct letters in the correct spot.")
    print("Gray letters are incorrect letters.")
    print("Let the guessing commence!\n")

    replay = True
    while replay == True:

        char_bank = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        i = random.randint(0, 1002) #by having char_bank and i in the while loop, they reset each time the user replays

        with open("word_list") as word_list: #this generates a selected_word
            selected_word = word_list.readlines()
            selected_word = selected_word[i].strip()

        attempts = 0
        guess_num = [""] * 6
        while attempts in range(6):
            guess = input("Guess: ").lower()
            while len(guess) != 6 or not guess.isalpha():
                print("Please input a 6-letter word.")
                guess = input("Guess: ").lower()

            guess_num[attempts] = guess #assigns an index in the list guess_num to the guessed word, so that past words can be printed before the guessed word
            list(guess) #creates a list of the letters in the guessed word

            for j in range(attempts + 1): #this loop prints past words, along with the currently guessed word
                print(line_divider)
                guess = guess_num[j]

                for n in range(4): #this loops prints each line of the ascii letter
                    for h in range(6): #this loop prints each letter; changing the parameter will change how many letters are printed
                        print("|", end="") #prints the | before each line of the ascii letter

                        if guess[h] == selected_word[h]: #prints the line of the ascii letter in purple
                            print("\033[35m" + letters[thisdict[guess[h]]][n] + "\x1b[0m", end="")

                        elif guess[h] in selected_word: #prints the line of the ascii letter in red
                            print("\033[31m" + letters[thisdict[guess[h]]][n] + "\x1b[0m", end="")

                        else: #prints the line of the ascii letter in plain gray
                            print("" + letters[thisdict[guess[h]]][n] + "", end="")

                        if guess[h] in char_bank: #removes the letters from the "unused letters"
                            char_bank.remove(guess[h])

                    print(end="|\n") #prints the | at the end of every line
            attempts += 1 #end of the printing loops

            for i in range(attempts, 6): #prints blank spots that show up after the guesses
                print(line_divider)
                for e in range(4): #this parameter selects how many empty lines are between each line_divider
                    print(char_divider)
            print(line_divider)

            print("Unused letters: ", end="")
            for q in range(len(char_bank)): #prints "unused letters" after each guess
                print(char_bank[q].upper(), end=" ")
            print()

            if attempts == 1 and guess == selected_word:
                print("\nYou won in", attempts, "guess!")
                break
            elif guess == selected_word:
                print("\nYou won in", attempts, "guesses!")
                break
            if attempts == 6:
                print("\nYou lost.", "The word was:", selected_word)
                    
        replay_response = input("\nPlay again? ") #replay mechanism
        if replay_response.lower() == "yes" or replay_response.lower() == "y":
            replay = True
        else:
            replay = False

wordle()

""" A python program that allows a user to guess a number
within a certain range provided by the program and handles the input accordingly"""

level = ""

while True:
    level = input("Choose a Level, \nEASY, MEDIUM or HARD: ").lower()
    if level == 'easy':
        secretNumber = 7
        guessCount = 0
        guessLimit = 6
        while guessCount < 6:
            guessLimit = guessLimit - 1
            print("\nGUESS A NUMBER FROM 1-10!")

            try:
                guessedNumber = int(input("Guess: "))
                if guessedNumber == secretNumber:
                    print("YOU GOT IT RIGHT!\n")
                    print("PLAY AGAIN...\n")

                    break

                else:
                    if guessLimit == 0:
                        print("THAT WAS WRONG!")
                        print("GAME OVER! \n")
                        print("PLAY AGAIN...\n")

                    else:
                        print("THAT WAS WRONG!")
                        print(f"YOU HAVE {guessLimit} GUESS(ES) REMAINING!\n ")

            except ValueError:
                print(f"\nYOUR INPUT IS NOT A NUMBER!, RESTART!")
                break

            guessCount += 1

    elif level == 'medium':
        secretNumber = 14
        guessCount = 0
        guessLimit = 4
        while guessCount < 4:
            guessLimit = guessLimit - 1
            print("\nGUESS A NUMBER FROM 1-20!")

            try:
                guessedNumber = int(input("Guess: "))
                if guessedNumber == secretNumber:
                    print("YOU GOT IT RIGHT!\n")
                    print("PLAY AGAIN...\n")
                    break

                else:
                    if guessLimit == 0:
                        print("THAT WAS WRONG!")
                        print("GAME OVER!")
                        print("PLAY AGAIN...\n")

                    else:
                        print("THAT WAS WRONG!")
                        print(f"YOU HAVE {guessLimit} GUESS(ES) REMAINING!\n ")

            except ValueError:
                print(f"\nYOUR INPUT IS NOT A NUMBER!, RESTART!")
                break

            guessCount += 1

    elif level == 'hard':
        secretNumber = 28
        guessCount = 0
        guessLimit = 3
        while guessCount < 3:
            guessLimit = guessLimit - 1
            print("\nGUESS A NUMBER FROM 1-50!")

            try:
                guessedNumber = int(input("Guess: "))
                if guessedNumber == secretNumber:
                    print("YOU GOT IT RIGHT!\n")
                    print("PLAY AGAIN...\n")
                    break

                else:
                    if guessLimit == 0:
                        print("THAT WAS WRONG!")
                        print("GAME OVER!")
                        print("PLAY AGAIN...\n")

                    else:
                        print("THAT WAS WRONG!")
                        print(f"YOU HAVE {guessLimit} GUESS(ES) REMAINING!\n ")

            except ValueError:
                print(f"\nYOUR INPUT IS NOT A NUMBER!, RESTART!")
                break

            guessCount += 1

    else:
        print('INVALID LEVEL!\n ')


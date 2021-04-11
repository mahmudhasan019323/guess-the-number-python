import random
logo = '''

 .d8888b.                                           888    888                                                    888                       
d88P  Y88b                                          888    888                                                    888                       
888    888                                          888    888                                                    888                       
888        888  888  .d88b.  .d8888b  .d8888b       888888 88888b.   .d88b.       88888b.  888  888 88888b.d88b.  88888b.   .d88b.  888d888 
888  88888 888  888 d8P  Y8b 88K      88K           888    888 "88b d8P  Y8b      888 "88b 888  888 888 "888 "88b 888 "88b d8P  Y8b 888P"   
888    888 888  888 88888888 "Y8888b. "Y8888b.      888    888  888 88888888      888  888 888  888 888  888  888 888  888 88888888 888     
Y88b  d88P Y88b 888 Y8b.          X88      X88      Y88b.  888  888 Y8b.          888  888 Y88b 888 888  888  888 888 d88P Y8b.     888     
 "Y8888P88  "Y88888  "Y8888   88888P'  88888P'       "Y888 888  888  "Y8888       888  888  "Y88888 888  888  888 88888P"   "Y8888  888     
                                                                                                                                            
                                                                                                                                            
                                                                                                                                            
                                                                                                                                                                                                                                                                                                                            
'''

def guess_the_num():
    print('\033c')
    print(logo)
    print('Welcome to the Number Guessing Game!')
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1,100)
    game_mode = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    attempts_left = (10 if game_mode=='easy' else 5) 
    
    while attempts_left != 0:
        print(f"You have {attempts_left} attempts remaining to guess the number")
        guess = int(input("make a guess: "))
        if guess == answer:
            print(f"you got it! the answer was {answer}")
            attempts_left = 0
        else:
            if guess > answer:
                print('Too high.')
                print('guess lower.')
                attempts_left -=1
            else:
                print('Too low.')
                print('guess higher.')
                attempts_left -= 1

            if attempts_left == 0:
                print("You've run out of guesses, you lose.")
                print(f"the answer was {answer}")

guess_the_num()
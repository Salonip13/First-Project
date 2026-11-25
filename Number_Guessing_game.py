from art import logo
import random
print(logo)
def get_user_guess():
    return  int(input("Choose a number between 1 to 10: "))
   

def check_guess(guess_num ,user_num):
    if guess_num == user_num:
            print("Yayyy!! You guessed it right")
            return True
    elif user_num > guess_num:
         print("To High!!")
         return False       
    else:
        print("To loww..")
        return False

def main():
    game_level = input("Choose a game level: Easy, Medium, Hard : ").lower()
    if game_level == "easy":
        guess_num = random.randint(1,10)
        max_attempts = 3
    elif game_level == "medium":
        guess_num = random.randint(1,50)
        max_attempts = 5
    elif game_level == "hard":
        guess_num = random.randint(1,100)
        max_attempts = 7
    else:
        print("Invalid game level. Please choose Easy, Medium, or Hard.")
        return

    attempts = 0
    while attempts < max_attempts:
        user_num = get_user_guess()
        attempts +=1
        if check_guess(guess_num ,user_num):
             print(f"You took {attempts} to guess.")
             break
    else:
        print(f"Sorry, you've used all your attempts. The number was {guess_num}.")


main()
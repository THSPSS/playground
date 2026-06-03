import random

from odd_or_even import convert_string_into_int


def main():
    count_the_guesses = 0
    game_is_on = True
    # generate random number between 1 and 9
    the_number = random.randint(1, 9)
    while game_is_on :
        if count_the_guesses > 3:
            print("Sorry , your try is over :(")
            game_is_on = False
        #ask user to guess the number
        int_user_guess = None
        while int_user_guess is None :
            user_guess = input("Guess the number between 1 to 9! : ")
            int_user_guess = convert_string_into_int(user_guess)
        #check if it is same
        if int_user_guess == the_number:
            print("Congratulation! You guessed right :)")
            # then return
            break

        #check answer and compare with the number
        if int_user_guess > the_number:
            # print guess number with upward
            print("Down the guess :)")
        #else if it is less then the number
        else:
            # else say lower the guessing number
            print("Up the guess :)")
        #count the try of user
        count_the_guesses += 1



if __name__ == "__main__":
    main()
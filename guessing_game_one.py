import random

from odd_or_even import convert_string_into_int


def main():
    count_the_guesses = 0
    user_guess = None
    int_user_guess = None
    # generate random number between 1 and 9
    the_number = random.randint(1, 9)
    while user_guess != "exit" or int_user_guess != the_number:
        # if count_the_guesses > 3:
        #     print("Sorry , your try is over :(")
        #     game_is_on = False
        #ask user to guess the number
        while int_user_guess is None :
            user_guess = input("Guess the number between 1 to 9! : ")
            int_user_guess = convert_string_into_int(user_guess)
        #check answer and compare with the number
        if int_user_guess > the_number:
            # print guess number with upward
            print("Your answer is higher than the number")
        #else if it is less then the number
        else:
            # else say lower the guessing number
            print("Your answer is lower than the number")
        #count the try of user
        count_the_guesses += 1

    if user_guess != "exit":
        print("Congratulation! You guessed right :)")
        print(f"You tried {count_the_guesses} times")
    print("===============GAME END=====================")


if __name__ == "__main__":
    main()
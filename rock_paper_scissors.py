import random

random_outcomes = ['rock' , 'paper' , 'scissors']


def main():
    print("This is for Solo Play.\n Please pick one as short term >\n rock \n paper \n scissors \n\n"
          "If you want to use random then enter random :)")
    game_set_count = 0
    your_score = 0
    other_score = 0
    #using while loop
    #good idea if we would add random choice from user :)
    while game_set_count < 3:
        game_dict = {'rock':1, 'paper':2 , 'scissors':3}

        #user
        player = input("your choice 😀: ")
        if player == "random":
            player_choice = game_dict.get(random.choice(random_outcomes))
        else :
            player_choice = game_dict.get(player.strip())

        #computer
        other_player_random_choice = random.choice(random_outcomes)
        other_choice = game_dict.get(other_player_random_choice)

        print(f"your choice 😀 ️: {player_choice}")
        print(f"computers choice 🖥️: {other_player_random_choice}")

        #check the winner
        result = player_choice - other_choice

        if result == 0 :
            print("It is Draw! \n")
            game_set_count += 0
        else :
            if result in [-2 , 1]:
                your_score += 1
                print("You Win! :) \n")

            if result in [-1 , 2]:
                other_score += 1
                print("You Lose :( \n")
            game_set_count += 1

        if game_set_count == 3:
            print(f"You : {your_score}  VS other score : {other_score}")
            if your_score > other_score:
                print("Congratulation! You Win! :) ")
            else:
                print("Sorry! You Lose :( ")
            keep_playing = input("Do you want to play more ? (Y/N) :").upper()
            if keep_playing == 'Y':
                game_set_count = 0
                your_score = 0
                other_score = 0


        # if player_choice == other_player_choice:
        #     print("It is a draw!")
        # elif player_choice == 'R':
        #     if other_player_choice == "S":
        #         print("You Win!")
        #     else:
        #         print("you Lose!")
        # elif player_choice == "P" :
        #     if other_player_choice == "R":
        #         print("You Win!")
        #     else:
        #         print("you Lose!")
        # elif player_choice == "S":
        #     if other_player_choice == "P":
        #         print("You Win!")
        #     else:
        #         print("you Lose!")
        # else:
        #     print("Invalid input! please enter again")
        # another_round = input("Do you want to play other round? (Y/N) : ").upper()
        # if another_round == "N":
        #     game_is_on = False



if __name__ == "__main__":
    main()
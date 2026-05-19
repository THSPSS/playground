import random

other_player_outcomes = ['R' , 'P' , 'S']


def main():
    game_is_on = True
    #using while loop
    while game_is_on:
        player_choice = input("Player choose among rock, paper, scissors using R for rock, P for paper and S for Scissors : ").upper()
    #ask first player to choose among rock paper scissors
    #keep input and ask other play choose among rock , paper, scissors
        other_player_choice = random.choice(other_player_outcomes)
        print(other_player_choice)
    #compare users choices
        if player_choice == other_player_choice:
            print("It is a draw!")
        elif player_choice == 'R':
            if other_player_choice == "S":
                print("You Win!")
            else:
                print("you Lose!")
        elif player_choice == "P" :
            if other_player_choice == "R":
                print("You Win!")
            else:
                print("you Lose!")
        elif player_choice == "S":
            if other_player_choice == "P":
                print("You Win!")
            else:
                print("you Lose!")
        else:
            print("Invalid input! please enter again")
        another_round = input("Do you want to play other round? (Y/N) : ").upper()
        if another_round == "N":
            game_is_on = False



if __name__ == "__main__":
    main()
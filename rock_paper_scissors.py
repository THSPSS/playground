import random

outcomes = ['r' , 'p' , 's']

def main():
    game_is_on = True
    #using while loop
    while game_is_on:
        player_choice = input("Player choose among rock, paper, scissors using R for rock, P for paper and S for Scissors : ").upper()
    #ask first player to choose among rock paper scissors
    #keep input and ask other play choose among rock , paper, scissors
        other_player_choice = input("Other player choose among rock, paper, scissors using R for rock, P for paper and S for Scissors : ").upper()
    #compare users choices
        if player_choice == "R":
            if other_player_choice == "S":
                winner = "first player"
            elif other_player_choice == "P":
                winner = "other player"
            else:
                winner = None
        elif player_choice == "P" :
            if other_player_choice == "R":
                winner = "first player"
            elif other_player_choice == "S":
                winner = "other player"
            else:
                winner = None
        else :
            if other_player_choice == "R":
                winner = "other player"
            elif other_player_choice == "P":
                winner = "first player"
            else:
                winner = None

        if winner is None:
            print("It is a draw!")
        elif winner == "first player":
            print("winner is first player")
        else:
            print("winner is other player")

        another_round = input("Do you want to play other round? (Y/N) : ").upper()
        if another_round == "N":
            game_is_on = False

        #pick winner

        #ask user about keep game on


if __name__ == "__main__":
    main()
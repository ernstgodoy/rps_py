import random

comp_wins = 0
player_wins = 0

def choose_option():
    player_choice = input("Choose Rock Paper or Scissors: ")
    if player_choice in ["Rock", "rock"]:
        player_choice = "r"
    elif player_choice in ["Paper", "paper"]:
        player_choice = "p"
    elif player_choice in ["Scissors", "scissors"]:
        player_choice = "s"
    else:
        print ("Please choose either Rock, Paper or Scissors.")
        choose_option()
    return player_choice 

def computer_option():
    comp_choice = random.randint(1,3)
    if comp_choice == 1:
        comp_choice = "r"
    elif comp_choice == 2:
        comp_choice = "p"
    else:
        comp_choice = "s"
    return comp_choice

while True:
    print("")
    player_choice = choose_option()
    comp_choice = computer_option()
    print("")

    if player_choice == "r":
        if comp_choice == "r":
            print ("Tie! You both chose Rock.")
        elif comp_choice == "p":
            print ("You loose! Computer chose Paper.")
            comp_wins += 1
        elif comp_choice == "s":
            print ("You win! Computer chose Scissors.")
            player_wins += 1
    elif player_choice == "p":
        if comp_choice == "p":
            print ("Tie! You both chose Paper.")
        elif comp_choice == "s":
            print ("You loose! Computer chose Scissors.")
            comp_wins += 1
        elif comp_choice == "r":
            print ("You win! Computer chose Rock.")
            player_wins += 1
    elif player_choice == "s":
        if comp_choice == "s":
            print ("Tie! You both chose Scissors.")
        elif comp_choice == "r":
            print ("You loose! Computer chose Rock.")
            comp_wins += 1
        elif comp_choice == "p":
            print ("You win! Computer chose Paper.")
            player_wins += 1

    print ("")
    print ("Player wins: " + str(player_wins))
    print ("Computer wins: " + str(comp_wins))
    print ("")

    player_choice = input("Play Again?(y/n)")
    if player_choice in ["Y","y","Yes","yes"]:
        pass
    elif player_choice in ["N", "n", "No", "no"]:
        print("")
        print("Goodbye :)")
        print("")
        break
    else:
        break



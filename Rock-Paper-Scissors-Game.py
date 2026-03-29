import random as rand

def Getting_Choices():
    player_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    computer_choice = rand.choice(['rock', 'paper', 'scissors'])
    print(f"You Chose {player_choice}, Computer Chose {computer_choice}")
    choices = {"player_choice": player_choice, "computer_choice": computer_choice}
    return choices

def Check_Win(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == "rock"):
        if(computer == "scissors"):
            return "Rock smashes Scissors!, You Win!😎"
        else:
            return "Paper covers Rock!, You Lose😭"
        
    elif(player == "paper"):
        if(computer == "rock"):
            return "Paper covers Rock!, You Win!😎"
        else:
            return "Scissors cut Paper!, You Lose😭"
         
    elif(player == "scissors"):
        if(computer == "paper"):
            return "Scissors cut Paper!, You Win!😎"
        else:
            return "Rock smashes Scissors!, You Lose😭"
    return "Incorrect Choice!"

choices = Getting_Choices()
print(Check_Win(choices["player_choice"], choices["computer_choice"]))
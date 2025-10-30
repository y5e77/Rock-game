
def get_computer_choice(round_number):
    """
    Generate a predictable computer choice using only basic logic.
    (No random module is used.)
    Choices rotate: rock -> paper -> scissors -> rock ...
    """
    choices = ["rock", "paper", "scissors"]
    return choices[round_number % 3]

def determine_winner(player, computer):
    """Decide the winner based on player and computer choices."""
    if player == computer:
        return "It's a tie!"
    elif (player == "rock" and computer == "scissors") \
        or (player == "scissors" and computer == "paper") \
        or (player == "paper" and computer == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    print("Welcome to , Paper, ScissoRockrs!")
    print("Type 'rock', 'paper', or 'scissors' to play.")
    print("Type 'quit' to stop playing.\n")

    round_number = 0
    player_score = 0
    computer_score = 0

    while True:
        player_choice = input("Your choice: ").lower()

        if player_choice == "quit":
            break
        elif player_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice! Please choose rock, paper, or scissors.")
            continue

        computer_choice = get_computer_choice(round_number)
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(player_choice, computer_choice)
        print(result)

        # Update scores
        if "win" in result and "You" in result:
            player_score += 1
        elif "Computer" in result:
            computer_score += 1

        print(f"Score -> You: {player_score} | Computer: {computer_score}\n")

        round_number += 1

    print("\nGame Over!")
    print(f"Final Score -> You: {player_score} | Computer: {computer_score}")
    print("Thanks for playing!")

if __name__ == "__main__":
    main()

def get_computer_choice(round_number, last_player_choice=None):
    """Adaptive computer choice: first round 'rock', then counters last player move."""
    if last_player_choice is None:
        return "rock"
    counter_moves = {"rock": "paper", "paper": "scissors", "scissors": "rock"}
    return counter_moves[last_player_choice]


def determine_winner(player, computer):
    """Decide the winner based on player and computer choices."""
    if player == computer:
        return "tie"
    elif (player == "rock" and computer == "scissors") \
        or (player == "scissors" and computer == "paper") \
        or (player == "paper" and computer == "rock"):
        return "player"
    else:
        return "computer"


def play_game():
    """Play a single match of Rock, Paper, Scissors."""
    print("\n🎮 Welcome to Rock, Paper, Scissors!")
    print("Type 'rock', 'paper', or 'scissors' to play.")
    print("Type 'quit' anytime to stop playing.\n")

    # Best-of-N setup
    while True:
        try:
            total_rounds = int(input("How many rounds would you like to play (odd number please)? "))
            if total_rounds % 2 == 1 and total_rounds > 0:
                break
            else:
                print("Please enter a positive odd number (e.g., 3, 5, 7).")
        except ValueError:
            print("Please enter a valid number!")

    player_score = 0
    computer_score = 0
    round_number = 0
    last_player_choice = None
    round_history = []

    while round_number < total_rounds:
        player_choice = input(f"\nRound {round_number + 1} - Your choice: ").strip().lower()

        if player_choice == "quit":
            break
        elif player_choice not in ["rock", "paper", "scissors"]:
            print("⚠️ Invalid choice! Please choose rock, paper, or scissors.")
            continue

        computer_choice = get_computer_choice(round_number, last_player_choice)
        print(f"🖥️ Computer chose: {computer_choice}")

        result = determine_winner(player_choice, computer_choice)

        if result == "player":
            print("✅ You win this round!")
            player_score += 1
            winner_icon = "✅"
        elif result == "computer":
            print("💻 Computer wins this round!")
            computer_score += 1
            winner_icon = "💻"
        else:
            print("🤝 It's a tie!")
            winner_icon = "🤝"

        round_history.append(
            f"Round {round_number + 1}: You ({player_choice}) vs Computer ({computer_choice}) -> {winner_icon} {result.title()}"
        )

        print(f"Score -> You: {player_score} | Computer: {computer_score}")
        last_player_choice = player_choice
        round_number += 1

        # Early win check
        if player_score > total_rounds // 2 or computer_score > total_rounds // 2:
            break

    # Game summary
    print("\n🏁 Game Over!")
    print(f"Final Score -> You: {player_score} | Computer: {computer_score}\n")
    print("📜 Round Summary:")
    for line in round_history:
        print(" -", line)

    if player_score > computer_score:
        print("\n🎉 Congratulations, you won the match!")
    elif computer_score > player_score:
        print("\n💻 The computer wins the match!")
    else:
        print("\n🤝 It's an overall tie!")


def main():
    """Allow replaying multiple games."""
    while True:
        play_game()
        replay = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if replay not in ["yes", "y"]:
            print("\nThanks for playing! 👋")
            break


if __name__ == "__main__":
    main()

print("Hello Rock Paper")
class Leaderboard:
    def __init__(self):
        self.scores = {}   # Dictionary to store player scores

    # Add or Update player
    def add_update_player(self, name, score):
        self.scores[name] = score
        print("Score updated successfully!")

    # Display Top K players
    def show_top_k(self, k):
        if not self.scores:
            print("Leaderboard is empty!")
            return

        # Sort players by score (highest first)
        sorted_players = sorted(self.scores.items(), key=lambda x: x[1], reverse=True)

        print("\n--- Leaderboard ---")
        for i in range(min(k, len(sorted_players))):
            name, score = sorted_players[i]
            print(f"{i+1}. {name} - {score}")
        print("-------------------\n")


# ---------------------------
# Main Program
# ---------------------------

lb = Leaderboard()

while True:
    print("1. Add/Update Player")
    print("2. Show Top K Players")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter player name: ")
        score = int(input("Enter score: "))
        lb.add_update_player(name, score)

    elif choice == "2":
        k = int(input("Enter value of K: "))
        lb.show_top_k(k)

    elif choice == "3":
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Try again...")
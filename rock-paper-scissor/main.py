from random import randint

title = "rock-paper-scissor"
print(title)
print(f"{'=' * len(title)}")

weapon = ("rock", "paper", "scissor")

player = input("Choose your weapon(rock | paper | scissor): ")
computer = weapon[randint(0,2)]

if player == computer:
    print("Player uses", player)
    print("Computer uses", computer)
    print("Nobody wins!")
elif player == "rock":
    if computer == "paper":
        print("Player uses", player)
        print("Computer uses", computer)
        print("Computer wins!")
    elif computer == "scissor":
        print("Player uses", player)
        print("Computer uses", computer)
        print("Player wins!")
elif player == "paper":
    if computer == "rock":
        print("Player uses", player)
        print("Computer uses", computer)
        print("Player wins!")
    elif computer == "scissor":
        print("Player uses", player)
        print("Computer uses", computer)
        print("Computer wins!")
elif player == "scissor":
    if computer == "rock":
        print("Player uses", player)
        print("Computer uses", computer)
        print("Computer wins!")
    elif computer == "paper":
        print("Player uses", player)
        print("Computer uses", computer)
        print("Player wins!")
else:
    print("Wrong weapon!")

        
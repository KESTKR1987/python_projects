from random import randint

print("Rock...")
print("Paper...")
print("Scissors...")
print("SHOOT!")
	
player = input("Player, make your move: ").lower()
rand_num = randint(0,2)

if rand_num == 0:
	computer = "rock"
elif rand_num == 1:
	computer = "paper"
else:
	computer = "scissors"
print(f"Computer plays {computer}")

if player == computer:
	print("It's a tie! GO AGAIN!")
elif player == "rock" and computer == "scissors":
	print("PLAYER WINS!")
elif player == "paper" and computer == "rock":
	print("PLAYER WINS")
elif player == "scissors" and computer == "paper":
	print("PLAYER WINS!")
else:
	print("COMPUTER WINS!")
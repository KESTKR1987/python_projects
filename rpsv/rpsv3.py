print("Rock...")
print("Paper...")
print("Scissors...")
print("SHOOT!")
	#Player enters option
player1 = input("Player 1, make your move: ")
print("***NO CHEATING!***\n\n" * 25)
player2 = input("Player 2, make your move: ")
	#player options
if player1 == player2:
	print("It's a tie! GO AGAIN!")
elif player1 == "rock" and player2 == "scissors":
	print("player 1 wins!")
elif player1 == "paper" and player2 == "rock":
	print("player 1 wins!")
elif player1 == "scissors" and player2 == "paper":
	print("player 1 wins!")
else:
	print("player 2 wins!")
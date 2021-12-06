player1=input("Enter R/P/S: ")
player2=input("Enter R/P/S: ")
if player1==player2:
    print("Its a draw!")
if player1=="R":
    if player2=="P":
        print("Player 2 wins!")
elif player2=="S":
    print("Player1 wins!")
elif player1=="P":
    if player2=="S":
        print("Player 2 wins!")
    elif player2=="R":
        print("Player 1 wins!")
elif player1=="S":
    if player2=="R":
        print("Player 2 wins!")
    elif player2=="P":
        print("Player1 wins!")


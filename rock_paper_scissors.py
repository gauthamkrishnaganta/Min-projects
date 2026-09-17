count_p1 =0
count_p2 =0
count = 0
for i in range(5):
    player1 = input("Enter your move : ").lower().strip()
    player2 = random.choice(["Rock", "Paper", "Scissors"]).lower()
    print(player2)
    if player1 == player2:
        print("draw")
    elif player1 == "rock" and player2 == "paper":
        count_p2 += 1
    elif player1 == "paper" and player2 == "rock":
        count_p1 += 1
    elif player1 == "paper" and player2 == "scissors":
        count_p2 += 1
    elif player1 == "scissors" and player2 == "paper":
        count_p1 += 1
    elif player1 == "scissors" and player2 == "rock":
        count_p2 += 1
    elif player1 == "rock" and player2 == "scissors":
        count_p1 += 1
    print(f'Player 1: {count_p1}')
    print(f'Player 2: {count_p2}')

if count_p1 > count_p2:
    print("player 1 wins")
else:
    print("player 2 wins")


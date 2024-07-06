import random
choice = ['rock', 'paper', 'scissor']
c = random.choice(choice)
player_score = 0
computer_score = 0
Result = ''
guess = None

while guess not in (choice):
    while True:
        guess = input("Enter your Guess: ").strip().lower()
        
        if guess == c:
            print("It's a tie")
            print(f'''computer's choice = {c}
Player's choice = {guess}''')
        elif guess == 'rock' and c == 'paper':
            print("Computer win this game")
            Result = 'computer'
            print(f'''computer's choice = {c}
Player's choice = {guess}''')
        elif guess == 'rock' and c == 'scissor':
            print("Player win this game")
            Result = 'player'
            print(f'''computer's choice = {c}
Player's choice = {guess}''')
        elif guess == 'paper' and c == 'scissor':
            print("Computer win this game")
            Result = 'computer'
            print(f'''computer's choice = {c}
Player's choice = {guess}''')
        elif guess == 'paper' and c== 'rock':
            print("Player win this game")
            Result = 'player'
            print(f'''computer's choice = {c}
Player's choice = {guess}''')
        elif guess == 'scissor' and c == 'paper':
            print("Player win this game")
            Result = 'player'
            print(f'''computer's choice = {c}
Player's choice = {guess}''')
        elif guess == 'scissor' and c== 'rock':
            print("Computer win this game")
            Result = 'computer'
            print(f'''computer's choice = {c}
Player's choice = {guess}''')
        if Result =='player':
            player_score += 1
        elif Result == 'computer':
            computer_score += 1
                
        Response= None
        Response = input("Do you want to play again? (y/n): ").strip().lower()
        if Response == 'y' :
            continue
        else:
            print(f"computer has won {computer_score} rounds and player has won {player_score} rounds. ")
            break
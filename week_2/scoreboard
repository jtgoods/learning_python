#importing sys module so i can exit the code for the endgame function
import sys
#intro text
print("Welcome to the Live Score Tracker")
print()
#team names
team1 = input("Enter Team 1 name")
print(team1)
team2 = input("Enter Team 2 name")
print(team2)
#winning score input
win = (int(input("Enter maximum score to win:")))
print(win)
print()
print("--- And heeeere we go!---")
print()
#variables for initial scores
score1 = 0
score2 = 0
#endgame function
def end_game():
    print("##############################")
    print(f"Final score: {team1}: {score1} | {team2}: {score2}")
    print("##############################")
#function for user input for scores, input validation for negative scores and "game over" end
def add_score(team_name): 
    add = 0
    while add <= 0:
        #score input
        add = (input(f"Points for {team_name}?"))
        if add.lower() == "game over":
            end_game()
            sys.exit()
        #positive integer returns
        try:
            num = int(add)
            if num >= 0:
                return num
            #negative integer re-prompts
            else:
                print("Points must be a non-negative integer!")
        except:
            print("That's not a valid number.")
#while loop to continue until one of the team's scores exceeds the Win input, above
while score1 < win and score2 < win:
    score1 += add_score(team1)
    score2 += add_score(team2)
    print(f"Scores: {team1}: {score1} | {team2}: {score2}")
    #Tie game check
    if score1 >= win and score2 >= win and score1 == score2:
        print("\nIt's a tie!")
        end_game()
        break
    #Team 1 wins endgame
    elif score1 >= win:
        print()
        print(f"{team1} wins!")
        end_game()  
        break
    #Team 2 wins endgame
    elif score2 >= win:
        print()
        print(f"{team2} wins!")
        end_game()
        break 

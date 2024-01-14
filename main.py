import random
import time

def show_board(choice_list):
    for b in range(0,8,3):
        board = f'|{choice_list[b]} |{choice_list[b+1]} |{choice_list[b+2]} |\n _________'
        print(board)


def user_win():
    if choice_list[0] == p1_choice and choice_list[1] == p1_choice and choice_list[2] == p1_choice:
        print("You Won !!! Game Over")
        return True
    elif choice_list[3] == p1_choice and choice_list[4] == p1_choice and choice_list[5] == p1_choice:
        print("You Won !!! Game Over")
        return True
    elif choice_list[6] == p1_choice and choice_list[7] == p1_choice and choice_list[8] == p1_choice:
        print("You Won !!! Game Over")
        return True
    elif choice_list[0] == p1_choice and choice_list[3] == p1_choice and choice_list[6] == p1_choice:
        print("You Won !!! Game Over")
        return True
    elif choice_list[1] == p1_choice and choice_list[4] == p1_choice and choice_list[7] == p1_choice:
        print("You Won !!! Game Over")
        return True
    elif choice_list[2] == p1_choice and choice_list[5] == p1_choice and choice_list[8] == p1_choice:
        print("You Won !!! Game Over")
        return True
    elif choice_list[0] == p1_choice and choice_list[4] == p1_choice and choice_list[8] == p1_choice:
        print("You Won !!! Game Over")
        return True
    elif choice_list[2] == p1_choice and choice_list[4] == p1_choice and choice_list[6] == p1_choice:
        print("You Won !!! Game Over")
        return True
    else:
        return False

def computer_win():
    if choice_list[0] == p2_choice and choice_list[1] == p2_choice and choice_list[2] == p2_choice:
        print("You Won !!! Game Over")
        return True
    elif choice_list[3] == p2_choice and choice_list[4] == p2_choice and choice_list[5] == p2_choice:
        print("You Won !!! Game Over")
        return True
    elif choice_list[6] == p2_choice and choice_list[7] == p2_choice and choice_list[8] == p2_choice:
        print("You Won !!! Game Over")
        return True
    elif choice_list[0] == p2_choice and choice_list[3] == p2_choice and choice_list[6] == p2_choice:
        print("You Won !!! Game Over")
        return True
    elif choice_list[1] == p2_choice and choice_list[4] == p2_choice and choice_list[7] == p2_choice:
        print("You Won !!! Game Over")
        return True
    elif choice_list[2] == p2_choice and choice_list[5] == p2_choice and choice_list[8] == p2_choice:
        print("You Won !!! Game Over")
        return True
    elif choice_list[0] == p2_choice and choice_list[4] == p2_choice and choice_list[8] == p2_choice:
        print("You Won !!! Game Over")
        return True
    elif choice_list[2] == p2_choice and choice_list[4] == p2_choice and choice_list[6] == p2_choice:
        print("You Won !!! Game Over")
        return True
    else:
        return False

print("Let's play the game of Tic- Tac-Toe \n")

choice_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

show_board(choice_list)

p1_choice = input("Please make a selection - 'x / o' : ").lower()
if p1_choice == 'x':
    p2_choice = 'o'
elif p1_choice == 'o':
    p2_choice = 'x'
else:
    print("Incorrect selection. please pick 'x' or 'o'")

print (f"Your choice :{p1_choice}")
print (f"Computer choice :{p2_choice}")
final =[1, 2, 3, 4, 5, 6, 7, 8, 9]

game_over = False
user_choices =[]
while not game_over:
    try:
        player_selection = True
        if player_selection:

            n1 = int(input("Please select a position between 1-9 : "))
            if n1 in user_choices:
                print("Spot already taken.")
                player_selection = True
            else:
                choice_list[(n1-1)] = p1_choice
                print(choice_list)
                show_board(choice_list)
                user_choices.append(n1)
                final.remove(n1)
                if user_win():
                    break
                time.sleep(1)
                print("Computer Turn")

            n2 = random.choice(final)
            choice_list[(n2 - 1)] = p2_choice
            show_board(choice_list)
            user_choices.append(n2)
            final.remove(n2)
            if computer_win():
                break
            time.sleep(1)
    except IndexError :
        print("Match Draw !!!Game Over !!! ")








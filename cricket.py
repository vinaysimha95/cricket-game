import random

user_score = 0
comp_score = 0
all_scores = [1, 2, 3, 4, 5, 6]
head_tail = ["Heads", "Tails"]
bat_bowl = ["bat", "bowl"]
function_call = 0

def toss():
    global user_play
    global toss_index
    print("Let's have a toss to see who gets to Bat first\nFlipping the coin........")
    user_choice = input("What's your choice? (Heads or Tails): ")
    user_choice = user_choice.capitalize()
    print("user selected :",user_choice)
    while(True):
        try:
            head_tail.index(user_choice)
            break
        except ValueError:
            user_choice = input("Dude, enter either 'Heads' or 'Tails'): ")
    toss_value = random.choice(head_tail)
    print("It's " + toss_value + "!")
    if(user_choice == toss_value):
        #print("Congrats, you get to bat first!!!")
        user_selected = input("Would you like to bat or bowl :  ")
        if(user_selected == "bat"):
            print("You have selected to bat")
            toss_index = 0
            user_play = "bat"
        elif(user_selected == "bowl"):
            print("You have selected to bowl")
            toss_index = 1
            user_play = "bowl"
        else:
            print("Please select either to bat or bowl")
        
    else:
        print("You have lost the toss") 
        pc_value = random.choice(bat_bowl)
        if(pc_value == "bat"):
            print("Computer as opted to bat")
            toss_index = 1
            user_play = "bowl"
        else:
            print("Computer as opted to bowl")
            toss_index = 0
            user_play = "bat"
        
        
        

def play(a, b, c, d):
    global function_call
    global user_score
    global comp_score
    while(True):
        user_move = int(input(a + ", enter either of the following (1, 2, 3, 4, 5, 6)? "))
        while(True):
            try:
                all_scores.index(user_move)
                comp_move = random.choice(all_scores)
                break
            except ValueError:
                user_move = int(input("Please type only either of the following values (1, 2, 3, 4, 5, 6)"))

        print(b, comp_move)
        if(user_move == comp_move):
            print(c)
            final_score = user_score if toss_index == 0 else comp_score
            print(d ,final_score)
            return
        else:
            if toss_index == 0:
                user_score += user_move
            else:
                comp_score += comp_move
        if(function_call == 1 and toss_index == 0 and (user_score > comp_score)):
            print("You have scored " + str(user_score) + ", which is more than required target")
            break
        elif(function_call == 1 and toss_index == 1 and (comp_score > user_score)):
            print("Computer scored " + str(comp_score) + ", which is more than required target")
            break
        
def score():
    print("\nSCORE:\nYou\tComputer\n"+str(user_score)+"\t"+str(comp_score))
    if(user_score > comp_score):
        print("\n\nYOU WIN!!!\n\n")
        
    elif(user_score < comp_score):
        print("\n\nCOMPUTER WINS!!!\n\n")
            
    else:
        print("\n\nWell, it's a tie!!!\n\n")

toss()
if(toss_index == 0):
    play(user_play, "Computer bowled", "You got out", "Your score is ")
    toss_index = 1
    function_call = 1
    print("\nNow it's the computer's chance to BAT")
    play("Bowl", "Computer scored", "Computer got out", "Computer's score is ")
else:
    play(user_play, "Computer scored", "Computer got out", "Computer's score is ")
    toss_index = 0
    function_call = 1
    print("\nNow it's your chance to BAT")
    play("Bat", "Computer bowled", "You got out", "Your score is ")

score()

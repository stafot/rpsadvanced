import random
mychoice = raw_input('I am playing with:')
def name_to_number(name) :
    if name == "rock" : return 0
    elif name == "fire" : return 1
    elif name == "scissors" : return 2
    elif name == "snake" : return 3
    elif name == "human" : return 4
    elif name == "tree"  : return 5
    elif name == "wolf"  : return 6
    elif name == "sponge" : return 7
    elif name == "paper" : return 8
    elif name == "air" : return 9
    elif name == "water" : return 10
    elif name == "dragon"  : return 11
    elif name == "devil"  : return 12
    elif name == "lightning" : return 13
    elif name == "gun"  : return 14
    else : return 15;
    
def number_to_name(num) :
    if num == 0 : return "rock"
    elif num == 1 : return "fire"
    elif num == 2 : return "scissors"
    elif num == 3 : return "snake"
    elif num == 4 : return "human"
    elif num == 5 : return "tree"
    elif num == 6 : return "wolf"
    elif num == 7 : return "sponge"
    elif num == 8 : return "paper"
    elif num == 9 : return "air"
    elif num == 10 : return "water"
    elif num == 11 : return "dragon"
    elif num == 12 : return "devil"
    elif num == 13 : return "lightning"
    elif num == 14 : return "gun"
    else : return "Fail!"
def rpsls(name): 
   player_number = name_to_number(name)
   comp_number = random.randrange(0,14)
   comp_selection = number_to_name(comp_number)
   dif = (player_number - comp_number)%15
   if player_number < 15 and dif == 0 :
        outcome = "Player and computer tie!"
   elif player_number < 15 and dif == 1:
        outcome = "Computer wins!"
   elif player_number < 15 and dif == 2:
        outcome = "Computer wins!"
   elif player_number < 15 and dif == 3:
        outcome = "Computer wins!"
   elif player_number < 15 and dif == 4:
        outcome = "Computer wins!"
   elif player_number < 15 and dif == 5:
        outcome = "Computer wins!"
   elif player_number < 15 and dif == 6:
        outcome = "Computer wins!"    
   elif player_number < 15 and dif == 7:
        outcome = "Computer wins!"
   elif player_number < 15 and dif == 8:
        outcome = "Player wins!"
   elif player_number < 15 and dif == 9:
        outcome = "Player wins!"        
   elif player_number < 15 and dif == 10:
        outcome = "Player wins!"
   elif player_number < 15 and dif == 11:
        outcome = "Player wins!"
   elif player_number < 15 and dif == 12:
        outcome = "Player wins!"
   elif player_number < 15 and dif == 13:
        outcome = "Player wins!"
   elif player_number < 15 and dif == 14:
        outcome = "Player wins!"
   else :
		return mychoice+" is not a valid option. Valid options are:\n rock\n fire\n scissors\n snake\n human\n tree\n wolf\n sponge\n paper\n air\n water\n dragon\n devil\n lightning\n gun"
   return "Player chooses: %s\nComputer chooses: %s\n%s" % (str(name), str(comp_selection), outcome)

def main():
    global mychoice
    while mychoice != 'exit' and mychoice != 'quit': 
        print rpsls(mychoice) 
        mychoice = raw_input('I am playing with:')

main() 

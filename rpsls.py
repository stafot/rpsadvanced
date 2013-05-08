import random
global name_and_number
name_and_number = [("rock", 0), ("fire", 1), ("scissors", 2), ("snake", 3), ("human", 4), ("tree", 5), ("wolf", 6), ("sponge", 7), ("paper", 8), ("air", 9), ("water", 10), ("dragon", 11), ("devil", 12), ("lightning", 13), ("gun", 14)]

def name_exists(name):
    return name in [nameTmp[0] for nameTmp in name_and_number]
def name_to_number(name):
    return [numTmp[0] for numTmp in name_and_number].index(name)
def number_to_name(number):
    return [nameTmp[0] for nameTmp in name_and_number][number]

def rpsls(name):
    nameL = name.lower()
    if name_exists(nameL):
        player_number = name_to_number(nameL)
        comp_number = random.randrange(0,14)
        dif = (player_number - comp_number)%15
        if dif == 0:
            outcome = "Player and computer tie!"
        elif dif > 0 and dif < 8:
            outcome = "Computer wins!"
        else:
            outcome = "Player wins!"
        return "Player chooses: %s\nComputer chooses: %s\n%s" % (str(nameL), number_to_name(comp_number), outcome)
    else:
        return name + " is not a valid option.\n" + GetHelp()

def GetHelp():
    return "Valid options are:\n rock\n fire\n scissors\n snake\n human\n tree\n wolf\n sponge\n paper\n air\n water\n dragon\n devil\n lightning\n gun\n ----\n exit\n quit \n----\n help\n ?"

def main():
    print "Type 'help' for help, 'quit' or 'exit' to end"
    mychoice = raw_input('I am playing with:')
    while mychoice != 'exit' and mychoice != 'quit':
        if mychoice == 'help' or '?':
            print GetHelp()
        else:
            print rpsls(mychoice)
        mychoice = raw_input('I am playing with:')

main()

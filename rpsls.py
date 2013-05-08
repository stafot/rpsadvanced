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
        Players = ["Player", "Computer"]
        choices = [name_to_number(nameL), random.randrange(0,14)]
        choicesStr = [number_to_name(choices[0]), number_to_name(choices[1])]
        print getResultInStr(Players, ChoicesStr, game_engine(Choices[0], Choices[1])
    else:
        return name + " is not a valid option.\n" + GetHelp()

# Although there's no change to the previous version,
# we add those 2 functions (game_engine, getRetInStr)
# so that future implementations/features will be
# easier to apply.
def game_engine(choices):
    dif = (choices[0] - choices[1])%15
    if dif == 0: return 0
    elif dif > 7: return 1
    else: return 2

def getResultInStr(players, choicesStr, outcomeNum):
    if outcomeNum == 0: outcome = "%s and %s tie!" % (players[0], players[1])
    else: outcome = "%s wins!" % (players[outcomeNum-1])
    return "%s chooses: %s\n%s chooses: %s\n%s" % (players[0], choicesStr[0], players[1], choicesStr[1], outcome)

def GetHelp():
    # TODO: Help string should not be hardcoded, but should be read from name_and_number tuple list
    return "Valid options are:\n rock\n fire\n scissors\n snake\n human\n tree\n wolf\n sponge\n paper\n air\n water\n dragon\n devil\n lightning\n gun\n ----\n exit\n quit \n----\n help\n ?"

def main():
    print "Type 'help' or '?' for help, 'quit' or 'exit' to end"
    mychoice = raw_input('I am playing with:')
    while mychoice != 'exit' and mychoice != 'quit':
        if mychoice == 'help' or mychoice == '?':
            print GetHelp()
        else:
            print rpsls(mychoice)
        mychoice = raw_input('I am playing with:')

main()

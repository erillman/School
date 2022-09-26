#File: Handicap.py
#This code should return your average and handicap score:

def main():
    bowler_name = input("Enter Bowler's name: ")
    game1 = int(input("Enter Game 1: "))
    game2 = int(input("Enter Game 2: "))
    game3 = int(input("Enter Game 3: "))

    average = (game1+game2+game3)/3
    handicap = (200-average)*.8
    
    print(("Handicap report for {}:".format(bowler_name)))
    print(" " + "{}'s average is: {}".format(bowler_name, int(average)))
    print((" "+ "{}'s handicap is: {}").format(bowler_name, int(handicap)))

main()

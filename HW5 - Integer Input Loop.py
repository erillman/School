#HW5 - Integer Input Loop
#This code should accept an arbitrary number of integer inputs and
#print out: # of inputs, max integer entered, min integer entered


def main():
    user_input = 0
    num = 0
    max_num = 0

    while user_input != 'stop':
        user_input = input("Enter an integer or 'stop' to end: ")
        if user_input == 'stop':
            break
        else:
            i = int(user_input)
        if num == 0 and i > max_num:
            max_num = i
            min_num = i
        elif i > max_num:
            max_num = i
        elif i < min_num:
            min_num = i
        num += 1
    
    if num == 0:
        print("You didn't print any numbers")
    else:
        print("You printed {} numbers".format(num))
        print("The maximum is {} and the minimum is {}.".format(max_num, min_num))







main()
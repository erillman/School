from random import randint

score = 100
tries = 10
print("Your starting score is: " + str(score))
while 0 < tries:
    while True:
        try:
            guess = int(input("Guess a number 1-100: "))
        except ValueError:
            print("Wtf is that")
        else:
            if 1 <= guess <= 100:
                break
            else:
                print("Out of range. Try again")
    tries -=1
    x = randint(1,100)
    if guess == x:
        print("You got the number!")
        score +=50
    else:
        print("Wrong!")
        score -=10
    print("The number was " + str(x))
    print("Your current score: " + str(score))
    print("You have " + str(tries) + " tries left")


print("Your final score is " + str(score))
print("Thanks for playing my game!")

#factorial



def main():
    n = int(input("Please enter a number: "))
    i = 1
    ans = 1

    while i < n:
        i +=1
        ans *=i
    print("The factorial of {} is {}".format(n,ans))
    print("This was looped through {} times".format(i))

main()
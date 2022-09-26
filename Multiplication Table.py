#multiplication table
limit = 10

def main():
    print("   |", end = " ")
    for i in range(1, limit):
        print(format(i, "4d"), end = " ")
    print()
    print("----------------------------------------------------")
    
    for row in range(1, limit):
        print(str(row) + "  |", end = " ")
        for col in range(1, limit):
            print(format(row*col, "4d"), end = " ")
        print()

main()
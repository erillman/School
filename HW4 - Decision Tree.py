#HW4 - Decision Tree


def main():
    age = int(input("Please enter person's age: "))
    income = input("Person's income (High, Medium, Low): ")
    student = input("Student or not? (Yes/No): ")
    credit = input("Credit? (Good/Poor): ")

    breakpoint()
    if age >= 31 and age <= 40:
        print("Will buy")
    elif age > 40 and credit == "Poor":
        print("Will buy")
    elif age <= 30 and student == "No":
        print("Will NOT buy")
    elif age > 40:
        print("Will NOT buy")
    else:
        print("Will buy")

main()


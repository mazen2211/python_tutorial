choice = "Y"

while choice.upper() == "Y":

    quiz_1 = float(input("Enter Quiz 1 mark: "))
    quiz_2 = float(input("Enter Quiz 2 mark: "))
    quiz_3 = float(input("Enter Quiz 3 mark: "))

    average = (quiz_1 + quiz_2 + quiz_3) / 3

    print("Average =", average)

    if average >= 50:
        print("PASS")
    else:
        print("FAIL")

    choice = input("Continue? Select Y/N: ")

print("Program Ended")

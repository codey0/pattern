try:
    def pattern(num):
        character = (input("Using which character: "))
        for i in range(0, num):
            for j in range(0, num):
                print(character, end='')
            num -= 1
            print("")
    pattern(int(input("How many iterations would you like the pattern to have: ")))
except ValueError:
    print("Invalid Input")
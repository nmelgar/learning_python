welcome = print("WELCOME TO THE EVEN OR ODD NUMBER VERIFIER\n ******")

user_input = int(input("Enter a number to see if it even or odd: "))

#for number in range(1, 100):
if (user_input % 2 == 0):
    print("This is an Even number")
elif(user_input % 2 != 0):
    print("This is an Odd number")
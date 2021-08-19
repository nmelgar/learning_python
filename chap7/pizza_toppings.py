message = "\nWrite the toppings you want in your pizza:"
message += "\nI will stop when you write 'quit'"
active = True

while active == True:
    toppings = input(message)
    if toppings == 'quit':
        break
    else:
        print(f"\n{toppings} is a great choice")

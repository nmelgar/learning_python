list1 = []
tuple1 = ()

number1 = input("First number to append: ")
number2 = input("Second number to append: ")
number3 = input("Third number to append: ")

list1.append(number1)
list1.append(number2)
list1.append(number3)

tuple1 = (number1, number2, number3)


print(f"the list will be the list: {list1}")
print(f"This will be a tuple: {tuple1}")
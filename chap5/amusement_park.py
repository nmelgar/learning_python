age = 66

#This is one way to do it and if-elif-else chain
print(f"This is a way to print how much your admission will cost")
if age < 4:
	print("Your admission is $0")
elif age < 18:
	print("Your admission cost is $25.")
else:
	print("Your admission is $40")

print(f"This is another way to print how much your admission will cost")
#the chain is evaluated but the price is in a variable this time
if age < 4:
	price = 0
elif age < 18:
	price = 25
elif age <65:
	price = 40
elif age >=65:
	price = 20
#you can omit the following 2 lines of code and use the previous one
#else:
#	price = 20
print(f"your admission cost is ${price}")
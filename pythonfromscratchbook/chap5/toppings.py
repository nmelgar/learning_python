#check if there are elements in the list
requested_toppings = []

if requested_toppings:
	for requested_topping in requested_toppings:
		print(f"addin {requested_topping}")
	print(f"\nFinished making your pizza!")
else:
	print("Are you sure you want a plain pizza?")

print("\n")
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

#if requested_topping != 'anchovies':
#	print("Hold the anchovies!")
#if 'mushrooms' in requested_toppings:
#	print("Adding mushrooms.")
#if 'pepperoni' in requested_toppings:
#	print("Adding pepperoni.")
#if 'extra cheese' in requested_toppings:
#	print("Adding extre cheese.")
#if we were using an elif statement it will just run the first if	

#this is a more efficente way to print the previous lines

for requested_topping in requested_toppings:
	#this will check for green peppers
	if requested_topping == 'green peppers':
		print("Sorry, we are out of green peppers right now")
	else:
		print(f"Adding {requested_topping}.")

print("\nFinished making your pizza")

print("\n")
#we are going to add 2 lists to compare to each other
available_toppings = ['mushrooms', 'green peppers', 'extra cheese', 'olives', 'pineapple']
requested_toppings = ['mushrooms', 'green peppers', 'french fries']

for requested_topping in requested_toppings:
	#check if the requested topping is actually n the available toppings
	if requested_topping in available_toppings:
		print(f"Adding {requested_topping}.")
	#if the topping is not in the available toppings print this
	else:
		print(f"Sorry we dont have {requested_topping}")
print("\nFinished making your pizza!")
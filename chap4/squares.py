
squares = [] #this is an empty list
for value in range(1, 11): #loop through each element from 1 to 1 
	#square = value ** 2
	#squares.append(square)
	squares.append(value**2)
print(squares)

print(f"The min number in the list is {min(squares)}\n")
print(f"The max number in the list is {max(squares)}\n")
print(f"The sum of numbers in the list is {sum(squares)}\n")

#list comprehensions
squares = [value**2 for value in range(1,11)]
print(squares)
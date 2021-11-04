#print from 1 to 20
for value in range(1,21):
	print(value)
#print from 1 to 1,000,000
#for values in range(1, 1000001):
#	print(values)

#print odd numbers
odd_numbers = list(range(1, 20, 2))
print(odd_numbers)

#print even numbers
even_numbers = list(range(0, 20, 2))
print(even_numbers)

#print a 1,000,000 using a loop
for values in range(1, 1000001):
	print(values)

#print a 1,000,000 using a list and range, adding max, min and sum
numbers = list(range(1, 1000001))
print(numbers)
print(f"The max value is {max(numbers)}")
print(f"The min value is {min(numbers)}")
print(f"The sum of the values in the list is {sum(numbers)}")

#list of multiples of 3 from 3 to 30
print(f"\n")
print(f"--List of multiples of 3 from 3 to 30")
for threes in range(3, 31, 3):
	print(threes)
print(f"\n")

#cube of the first 10 numbers
print(f"--Cube of numbers 1 to 10--")
for cubes in range(1, 11):
	print(cubes**3)
print(f"\n")

#list of comprehensions for cube of the first 10 numbers
print(f"--Comprehensive List of Cube of numbers 1 to 10--")
cubes = [numbers**3 for numbers in range(1,11)]
print(cubes)
print(f"\n")
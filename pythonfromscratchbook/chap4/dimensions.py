dimensions = (200, 50)
#This following line will show an error when trying to change a tuple
#dimensions[0] = 250
print(dimensions[0])
print(dimensions[1])

print("Original dimensions")
for dimension in dimensions:
	print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
	print(dimension)
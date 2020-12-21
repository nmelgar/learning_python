#Sort method changes the order permanently
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)


#Sorted function changes the order temporarily
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("\nHere is the original list")
print(cars)

print("\nHere is the sorted list")
print(sorted(cars))
print("\nHere is the original list again")
print(cars)

#Reverse Method changes the order permanently
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)

#len function to count the # of items in a list
print(len(cars))
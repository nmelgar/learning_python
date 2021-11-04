cars = ['audi', 'bmw', 'subaru', 'toyota']

print("\nList of cars, if BMW prints in upper case")
for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())
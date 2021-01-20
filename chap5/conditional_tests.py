cars = ['audi', 'bmw', 'chevrolet', 'ford']
car_not_favorite = 'subaru'
print("is car == 'subaru' ? I predict True")
print(car_not_favorite == 'subaru')

print(f"\nIs car == 'audi' ? I predict False")
print(car_not_favorite == 'audi')

print(f"\nIs car != 'chevrolet' ? I predic True")
print(car_not_favorite != 'chevrolet')

print(f"\nIs car != 'subaru' ? I predict False")
print(car_not_favorite != 'subaru')

print(f"\nPrint a list of my favorite cars:")
for favorite_cars in cars:
	if favorite_cars != 'audi':
		print(f"{favorite_cars.title()} is not my favorite car")
	else:
		print(f"{favorite_cars.title()} is my favorite car")

motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

#motorcycles[0] ='ducati'
#print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

cars = ['honda', 'mitsubishi', 'nissan', 'toyota']
print(cars)

cars.append('volkswagen')
print(cars)

#empty list
cars_types = []
cars_types.append('corolla')
cars_types.append('versa')
cars_types.append('camry')

print(cars_types)
cars_types.insert(2, 'megan')
cars_types.insert(0, 'navigator')
print(cars_types)

del motorcycles[0]
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

last_owned = motorcycles.pop(0)
print(f"the las motorcycles i owned was a {last_owned.title()}")
print(motorcycles)

#declare the list
motorcycles = ['honda','yamaha','suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me")

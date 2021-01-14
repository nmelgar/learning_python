#slicing a list
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players)
print(players[1:4])

#from beginning to the number 2
print(players[:2])

#starting from 2 through the end
print(players[2:])

#this will print the last 3 elements of the list
print(players[-3:])

print("here are the first three players on my team: ")
for player in players[:3]:
	print(player.title())

#copying a list
my_foods = ['pizza', 'tacos', 'enchiladas', 'tortas']
friend_foods = my_foods[:]
#we can add elements to the list to see if they are different
my_foods.append('canoli')
friend_foods.append('burguer')

print("My favorite foods are")
print(my_foods)

print("My friends favorite foods are")
print(friend_foods)

print(f"\n--This is a new list and slices--\n")

#print the first 3 elements of the list
golosinas = ['cacachuates', 'paletas', 'chicles', 'pulparindos', 'totis', 'gomitas']
print("The first 3 items in the list are:")
for golosina in golosinas[:3]:
	print(golosina.title())

#print the 2 items at the middle of the list
print("The itmes in the middle of the list are:")
for golosina in golosinas[2:4]:
	print(golosina.title())

#Print the last 3 items in the list
print("The last three items in the lis are")
for golosina in golosinas[-3:]:
	print(golosina.title())	

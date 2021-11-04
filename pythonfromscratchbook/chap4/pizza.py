pizzas = ['hawaian', 'just cheese', 'vegetarian', 'mushrooms']
friend_pizzas = pizzas[:]

pizzas.append('pastor')
friend_pizzas.append('3 meats')

#see if lists changed

print("My favorite pizzas are:")
for pizza in pizzas:
	print(f"I like {pizza} pizza")
print("I love pizza so much!")
print(f"\n--1st Pizza statements ends--\n")

print("My  friend's favorite pizzas are:")
for friends_pizza in friend_pizzas:
	print(f"He loves {friends_pizza.title()}pizza")
print("My friend loves pizza")
print(f"\n2nd Pizza statement ends--\n")


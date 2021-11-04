#define the list
magicians = ['alice', 'david', 'carolina']
#create FOR, with a temporarily variable called magician, which will be associated with the list magicians
for magician in magicians:
#will print each element of the list storing the values in the magician variable
	print(magician)

#you can create meaningful name for for loops lists
#for cat in cats:
#for dog in dogs:
#for item in list_of_items:
print("\n")
magicians = ['alice', 'david', 'carolina', 'carlos']
for magician in magicians:
	#everyting inside here is considered to be part of the loop
	print(f"{magician.title()}, that was a great trick!")
	print(f"I cant wait to see your next trick, {magician.title()}.\n")
#this is outside the loop
print("Thank you, everyone. That was a great magic show!")
print("\n")

#Print a new list of characters for a game, of course these are not magicians, but it's a good list to practice
characters = ['aragorn', 'frodo', 'legolas', 'sam']
print("Choose your character:")
for character in characters:
	print(f"{character.title()}")

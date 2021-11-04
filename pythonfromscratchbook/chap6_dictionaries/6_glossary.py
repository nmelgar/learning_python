glossary = {
    'dictionary': 'collection of key-value pairs that store information about something',
    'variable': 'think of it as a box that stores something',
    'lists': 'collection of data',
    'method': 'an action python can perform on a piece of data',
    'strings': 'text inside double or single quotes',
    #add 5 more terms as part of the activity
    'equality sign': 'looks like this ==',
    'inequality sign': 'looks like this !=',
    'using AND': 'multiple conditions must to be true',
    'using OR': 'one of the conditions must be true',
    'using NOT': 'if something is not',
}

#before knowing how to loop a dictionary
#print(f"A dictionary is: a {favorite_numbers['dictionary']}\n")
#print(f"A variable is: well, {favorite_numbers['variable']}\n")
#print(f"A list is: a {favorite_numbers['lists']}\n")
#print(f"A method is: {favorite_numbers['method']}\n")
#print(f"A string is: {favorite_numbers['strings']}\n")

for name, definition in glossary.items():
    print(f"\nName is: {name.title()} and its definition is: {definition}")
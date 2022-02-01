import enum


#reference: page 20 of the book
greet = "Hello world!"
for i in enumerate(greet[0:-1]):
    print (i)

#print last character
last_character = greet[len(greet)-1]
print(last_character)

new_greet = greet[:5] + ' wonderful' + greet[5:]
print(new_greet)
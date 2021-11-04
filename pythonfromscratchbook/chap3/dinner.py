print(f"\n--INITIAL ATTENDEES LIST--\n")
people_dinner = ['pepe', 'paco', 'pedro', 'luis']
print(people_dinner)
message1 = f"dear {people_dinner[0].title()} you are invited to a dinner with us"
print(message1)
message2 = f"dear {people_dinner[1].title()} you are invited to a dinner with us"
print(message2)
message3 = f"dear {people_dinner[2].title()} you are invited to a dinner with us"
print(message3)
print(f"dear {people_dinner[3].title()} you are invited to a dinner with us")

print(f"\n--CHANGES IN ATTENDEES LIST--")
wont_attend = 'luis'
people_dinner.remove(wont_attend)
people_dinner.append('bob')
print(people_dinner)
print(f"\n{wont_attend.upper()} wont attend due a personal commitmment with other friends")

print(f"\n--NEW ATTENDEES LIST--")
print(people_dinner)
print(f"dear {people_dinner[0].title()} thank you for joining us next week to the dinner ")
print(f"dear {people_dinner[1].title()} thank you for joining us next week to the dinner ")
print(f"dear {people_dinner[2].title()} thank you for joining us next week to the dinner ")
print(f"dear {people_dinner[3].title()} thank you for joining us next week to the dinner ")

print(f"\n--NEW CHANGES--")
print(f"I found a bigger table so I will be inviting more people to the meeting")

print(f"\n--NEW ATTENDEES LIST--")
people_dinner.insert(0, 'pancho')
people_dinner.insert(2, 'marcela')
people_dinner.append('mariana')
print(people_dinner)

print(f"\n--NEW INVITATIONS LIST--\n")
print(f"dear {people_dinner[0].title()} thank you for joining us next week to the dinner ")
print(f"dear {people_dinner[1].title()} thank you for joining us next week to the dinner ")
print(f"dear {people_dinner[2].title()} thank you for joining us next week to the dinner ")
print(f"dear {people_dinner[3].title()} thank you for joining us next week to the dinner ")
print(f"dear {people_dinner[4].title()} thank you for joining us next week to the dinner ")
print(f"dear {people_dinner[5].title()} thank you for joining us next week to the dinner ")
print(f"dear {people_dinner[6].title()} thank you for joining us next week to the dinner ")

print(f"\n--BIG CHANGES FOR THE DINNER--")
print(f"dear attendees thank you for the interest but just 2 persons will be invited ")

print(f"\n--CHANGES IN THE LIST--")
first_uninvited = people_dinner.pop(1)
print(f"Sorry, but {first_uninvited.title()} you will be joining us next time")
second_uninvited = people_dinner.pop(2)
print(f"Sorry, but {second_uninvited.title()} you will be joining us next time")
third_uninvited = people_dinner.pop(4)
print(f"Sorry, but {third_uninvited.title()} you will be joining us next time")
fourth_uninvited = people_dinner.pop(3)
print(f"Sorry, but {fourth_uninvited.title()} you will be joining us next time")
fifth_uninvited = people_dinner.pop(0)
print(f"Sorry, but {fifth_uninvited.title()} you will be joining us next time")
print(people_dinner)

#Printo how many attendees there will be to the dinner
attendees_total = len(people_dinner)
print(f"\nThere will be {attendees_total} invited people to the dinner")
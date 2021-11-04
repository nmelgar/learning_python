#<3 == free
#3 and 12 == $10
#>12 == $15

message = "Tell me your age and i will tell you how much"
message += "\nyou will pay for the movie"
print(message)
age = input("Whats you age? ")
person_age = int(age)

if person_age <= 3:
    print("Your ticket is free")
elif person_age >3 and person_age <=12:
    print("Your ticket is $10")
elif person_age > 12:
    print("Your ticket is $15")

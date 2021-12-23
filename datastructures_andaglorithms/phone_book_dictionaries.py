phoneBook = {
    "sam": 8713334455,
    "mat": 8713344455,
    "carl": 8713332422,
    "jeff": 8712334885,
    "john": 8715534775,
    "samantha": 8734334455,
    "matias": 8713774455,
    "carla": 8713336622,
    "jeffrey": 8718934885,
    "johnny": 8716634775,
    "samir": 8713004455,
    "matthew": 8713114455,
    "carly": 8712232422,
    "jeremy": 8713356885,
    "joanna": 8715589775
}

search = input("what name are you looking for?:")
if search in phoneBook.keys():
    for names, phoneNumbers in phoneBook.items():
        if names == search:
            print(f"{names} = {phoneNumbers}")
else:
    print("User not found, try again")

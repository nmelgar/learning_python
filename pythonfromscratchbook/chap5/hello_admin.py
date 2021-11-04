#print a personalized message if the username is admin
usernames = ['pedro', 'admin', 'karla', 'rodrigo', 'sandra']
#usernames = []

#check if the list is empty
if usernames:
	for username in usernames:
		print("This list is not empty")
else: 
	print("we need more users")


for username in usernames:
	if username == 'admin':
		print(f"Hello {username}, do you want to review the reports?")
	else:
		print(f"Hello {username}, it is nice to have you here :)")

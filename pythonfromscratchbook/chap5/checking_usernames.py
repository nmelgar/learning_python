current_users = ['john12', 'mark54', 'martha87', 'linda52', 'starkiller87']
new_users = ['jona12', 'mara6', 'LinDA52', 'tha25', 'starkiller87']

#to convert all the new usernames to lower case
#this will iterate through list - convert each element one at a time to lower
new_user_lowercase = [user.lower() for user in new_users] 

#to loop through a list it is necessary a FOR statement
for current_user in current_users:
	if current_user in new_user_lowercase:
		print(f"Sorry, the username {current_user} in not available")
	else:
		print(f"Cool!, the usernames {current_user} is available")
favorite_places = {
	'mark':{
		'place': 'russia',
		'age': 24
	},

	'andrea':{
		'place': 'finland',
		'age': 28
	},

	'pedro':{
		'place': 'rummania',
		'age': 32
	},


}

for user_name, fav_place in favorite_places.items():
	print(f"{user_name}'s favorite place is {fav_place['place']}")
cities = {
	'culiacan':{
		'state': 'sinaloa',
		'population' : 10000000,
		'country': 'mexico',
		'fact': 'weather is hot'
	},

	'gomez palacio':{
		'state': 'durango',
		'population' : 2500000,
		'country': 'mexico',
		'fact': 'it is dry sometimes'
	},


	'lerdo':{
		'state': 'durango',
		'population' : 200000,
		'country': 'mexico',
		'fact': 'weather is better than gomez palacio'
	},

	'torreon':{
		'state': 'coahuila',
		'population' : 2000000,
		'country': 'mexico',
		'fact': 'it has interesting places to visit'
	},

	'leon':{
		'state': 'guanajuato',
		'population' : 350000,
		'country': 'mexico',
		'fact': 'there hundred of thousands of shoes to buy'
	}

}

print("5 PLACES TO VISIT:")
for city, information in cities.items():
	print(f"\n{city.title()}, a beautiful place, with:")
	print(f"\t a {information['population']} population,")
	print(f"\t located at {information['state']} state in, {information['country'].title()},")
	print(f"\t with the interesting fact that {information['fact']}.")
rivers = {
    'Río Bravo': 'Mexico',
    'Nile river': 'Egypt',
    'Mississipi': 'United States',
}

print("We have these amazing rivers:")
for river in rivers.keys():
    print(f"{river.title()}")

print(f"\nBut also these amazing countries:")
for country in rivers.values():
    print(f"{country.title()}")

print(f"\nAnd these is how these rever match with a specific country\n")

for river, country in rivers.items():
    print(f"\nThe {river} runs through {country}")pr
prompt = "\nPlease enter the name of a city you have visited: "
prompt += "\nEnter 'quit' to say you are done. "

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I would love to go to {city.title()}.")

pizza = {
    'crust': 'thick',
    #this toppings has a list as its value
    'toppings': ['mushrooms', 'extra cheese'],
}

#summarize the order
print(f"You ordered a {pizza['crust']}-crust pizza "
    #the following line needs to be indented
    "with the following toppins:")

for topping in pizza['toppings']:
    print("\t" + topping)
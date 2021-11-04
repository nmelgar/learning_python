#celsius to fahrenheit formula
#(degrees°C × 9/5) + 32

#fahrenheit to celsius formula
#(degrees°F − 32) × 5/9

print("Welcome to the temperature converter")
temperature_selector = input("Are you in Fahrenheit or in Celsius? ")
print(str(temperature_selector))

if (temperature_selector == "celsius"):
    celsius_input = input("Write your temperature in celsius degrees  ")
    print("You chose: " + str(celsius_input) + "°C")
    celsius_formula = int(celsius_input) * 9/5 + 32
    print("The temperature in fahrenheit is " + str(celsius_formula) + "°F")
elif (temperature_selector == "fahrenheit"):
    fahrenheit_input = input("Write your temperature in fahrenheit degrees  ")
    print("You chose: " + str(fahrenheit_input) + "°F")
    fahrenheit_formula = (int(fahrenheit_input) - 32) * 5/9
    print("The temperature in celsius degrees is " + str(fahrenheit_formula) + "°C")
else:
    print("That's not a registered temperature paramenter, try celsisus or fahrenheit")



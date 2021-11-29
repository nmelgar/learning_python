alien_0 = {
    'x_position': 0,
    'x_position': 25,
    'speed': 'medium',
    'color': 'green',
    'points': 5
}

#to access the values in a dictionary
#name of the dictionary + the key
# print(alien_0['color'])
# print(alien_0['points'])

# new_points = alien_0['points']
# print(f"You just earned {new_points} points")

#ADD NEW KEY-VALUE PAIRS
# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
# print(alien_0)

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
elif alien_0['speed' == 'fast']:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"The new aliens position is {alien_0['x_position']}")

#removing key-value pairs | it is remove permanently
# del alien_0['points']



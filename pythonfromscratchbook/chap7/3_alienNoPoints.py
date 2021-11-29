alien_0 = {'color': 'green', 'speed': 'slow'}

#this will return an error if no value is assigned to points
# print(alien_0['points'])

#it takes 2 arguments, 1 = key, 2 (optional) value to be returned if key doesnt exist
print_value = alien_0.get('points', 'no point value assigned')
print(print_value)
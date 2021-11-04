alien_0 = {'color': 'green', 'points': 5}

print(alien_0)
#print(alien_0['color'])
#print(alien_0['points'])

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

#key-value pairs
#new_points = alien_0['points']
#print(f"You just earned {new_points}!")

#modyfing values in a dictionary
alien_0 = {'color': 'green'}
print(f"\nThe alien is {alien_0['color']}.")
alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")

###################alien speed ##########################
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"\nOriginal position: {alien_0['x_position']}")

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")
# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien.
    x_increment = 3
# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")

#adding more alient by creating  multiple dictionaries 
print(f"\n")
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)
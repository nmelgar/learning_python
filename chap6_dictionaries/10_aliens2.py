#make an empty list for storing aliens
aliens = []

#make 30 green aliens
for alien_number in range(30):
    #creates the new alien individually
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    #adds the new_alien dictionary to the aliens list
    #these actions are repeated 30 times to create the 30 aliens in the range
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15


#show the first 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...")

#show how many aliens have been created
print(f"Total number of aliens: {len(aliens)}")



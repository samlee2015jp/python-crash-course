alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'fast'}
print(f"Original position: {alien_0['x_position']}")
# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
x_increment = 0
increment = 0
if alien_0['speed'] == 'slow':
    increment = 1
elif alien_0['speed'] == 'medium':
    increment = 2
else:
# This must be a fast alien.
    x_increment = 3
# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")

alien_0 = {'color': 'green', 'speed': 'slow'}
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)

for alien in alien_0.values():
    print(alien)
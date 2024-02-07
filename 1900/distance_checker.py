
import math

r = float(input('What is the radius of your circular landmass? '))
h = float(input('Enter coordinates for the center of your landmass:\nx: '))
k = float(input('y: '))

x = float(input('Enter coordinates for the fish spawn point:\nx: '))
y = float(input('y: '))

d = (math.sqrt((math.pow(x - h, 2)) + (math.pow(y - k,2)))) - r 

print('The fish are a distance of', d,'from the shoreline.')
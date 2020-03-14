from random import uniform as rand
from matplotlib import pyplot as plot

# Fuction rand generates numbers between -1 and 1. The distribution of generated numbers is uniform.
# Using the rand function, plot a circle.

def generate_pi(magnitude=5):
    inside_points = []
    outside_points = []
    magnitude = 10**magnitude
    for _ in range(magnitude):
        x = rand(-1, 1)
        y = rand(-1, 1)
        if abs(x)**2 + abs(y)**2 <= 1:
            inside_points.append([x, y])
        else:
            outside_points.append([x, y])
        
    return inside_points, outside_points

inside, outside = generate_pi(magnitude=5)

plot.scatter(x=[i[0] for i in inside], y=[i[1] for i in inside], s=2)
plot.scatter(x=[i[0] for i in outside], y=[i[1] for i in outside], s=2)
plot.show()

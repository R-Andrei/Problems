from random import uniform as rand

# Fuction rand generates numbers between 0 and 1. The distribution of generated numbers is uniform.
# Using the rand function, approximate the value of pi.

def calculate_pi(magnitude=5):
    inside_area = 0
    magnitude = 10**magnitude
    for _ in range(magnitude):
        inside_area += 1 if rand(0, 1)**2 + rand(0, 1)**2 <= 1 else 0
    return 4 * inside_area / magnitude

pi = calculate_pi(magnitude=7)
print(pi)
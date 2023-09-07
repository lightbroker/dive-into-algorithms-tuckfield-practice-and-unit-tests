'''
    Plotting a hypothetical ball trajectory between the moment it is thrown (at x = 0) and when it hits the ground again

    Prereq:
    pip install matplotlib
'''

import matplotlib.pyplot as plt


def ball_trajectory(x):
    location = 10*x - 5*(x**2)
    return location

xs = [x/100 for x in list(range(201))]
ys = [ball_trajectory(x) for x in xs]

plt.plot(xs,ys)
plt.title('The Trajectory of a Thrown Ball')
plt.xlabel('Horizontal position of ball')
plt.ylabel('Vertical position of ball')
plt.axhline(y = 0)

plt.show()

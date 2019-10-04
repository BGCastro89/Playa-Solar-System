import numpy as np
import matplotlib.pyplot as plt

def debug_pp(r,theta):

    for i in xrange(0,len(r)):
        print theta[i], "\t", r[i]


def to_rads(angles):
    return  [np.radians(deg) for deg in angles]
    
def generate_plot(r,theta):

    debug_pp(r, theta)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='polar')

    c = ax.scatter(to_rads(theta), r)
    plt.savefig("solarsys.png")

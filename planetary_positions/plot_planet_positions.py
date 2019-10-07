import numpy as np
import matplotlib.pyplot as plt

def debug_pp(r,theta):

    for i in xrange(0,len(r)):
        # print int(np.round(r[i]))
        print theta[i], "\t", r[i]


def to_rads(angles):
    return  [np.radians(deg) for deg in angles]

def to_Gkm(distances):
    return  [r/1000000000 for r in distances]

def generate_plot(r,theta):

    debug_pp(r, theta)

    r = to_Mkm(r)
    theta = to_rads(theta)
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='polar',xmargin=1.2)
    ax.set_ylim(0,6)

    c = ax.scatter(theta, r)
    plt.savefig("solarsys.png")

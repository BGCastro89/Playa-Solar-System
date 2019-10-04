import numpy as np
import matplotlib.pyplot as plt

def debug_pp(r,theta):

    for i in xrange(0,len(r)):
        print theta[i], "\t", r[i]


def generate_plot(r,theta):
    # r, theta = [1.5,4.,6.,8.,11.], [33.,110.,130.,290.,340.]

    debug_pp(r, theta)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='polar')
    # ax = plt.polar()
    c = ax.scatter(theta, r)#, c=colors, s=area, cmap='hsv', alpha=0.75)
    # plt.savefig("solarsys.png")
    plt.savefig("test.png")

    plt.show()

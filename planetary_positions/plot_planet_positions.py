import numpy as np
import matplotlib.pyplot as plt

print("test")

def generate_plot(r,theta):


    r, theta = [1.5,4,6,8,11], [33,110,130,290,340]
    # Compute areas and colors
    # N = 5
    # r = 2 * np.random.rand(N)
    # theta = 2 * np.pi * np.random.rand(N)
    print(r, theta)
    # area = 61736162 * r**2 #5103339081 pluto
    # colors = thetaxs

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='polar')
    # ax = plt.polar()
    c = ax.scatter(theta, r)#, c=colors, s=area, cmap='hsv', alpha=0.75)
    # plt.savefig("solarsys.png")
    plt.savefig("test.png")

    # plt.show()



    #     # Fixing random state for reproducibility
    # np.random.seed(19680801)

    # # Compute areas and colors
    # N = 5
    # r = 2 * np.random.rand(N)
    # theta = 2 * np.pi * np.random.rand(N)
    # print(r, theta)
    # area = 200 * r**2
    # colors = theta

    # fig = plt.figure()
    # ax = fig.add_subplot(111, projection='polar')
    # c = ax.scatter(theta, r, c=colors, s=area, cmap='hsv', alpha=0.75)
    # plt.savefig("test.png")

    # plt.show()

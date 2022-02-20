import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

def arm(x,y):
    target = (x,y)
    ax.set_xlim(-3,3)
    ax.set_ylim(-3,3)
    distance = np.sqrt(target[0]**2+target[1]**2)
    if distance < 2 and x > 0 and y > 0:
        a1 = np.arctan(target[1]/target[0]) + \
            np.arctan(np.sqrt((4-target[0]**2-target[1]**2)/(target[0]**2+target[1]**2)))

        x = [0, np.cos(a1), target[0]]
        y = [0, np.sin(a1), target[1]]

        ax.plot(x,y, '-o')
        # ax.grid(True)
        ax.plot([-3,3],[0,0], '--')
        # plt.show()
    else:
        print('********** Out of Range **********')


def move(p1, p2):
    
    x = [p1[0],p2[0]]
    y = [p1[1],p2[1]]

    if (x[1]-x[0]) != 0:
        l = np.linspace(x[0], x[1], 20)
        m = (l-x[0])*(y[1]-y[0])/(x[1]-x[0])+y[0]
        
        for i,j in zip(l,m):
            ax.cla()
            ax.scatter(p2[0],p2[1], c='green')
            arm(i,j)
            # ax.set_title("frame {}".format(i)
            # Note that using time.sleep does *not* work here!
            plt.pause(0.01)
    else:
        print('***********  Invalid  **********')

def main(co_ord):
    for i in co_ord:
        move(i[0], i[1])

co_ord = [
    [(0.01,1),(1.9,0.1)],
    [(1.9,0.1),(np.sqrt(1.9),np.sqrt(1.9))],
    [(np.sqrt(1.9),np.sqrt(1.9)),(0.01,1)]
]

while True:
    main(co_ord)
# plt.show()


def CreateCheckerBoard(n):
    import matplotlib.pyplot as plt
    import numpy as np
    n = n
    x = np.tile(np.array([[0,255],[255,0]]),(n,n))
    print('Your Checkerboard array looks like so: \n')
    print(n,x)
    fig, ax = plt.subplots()
    ax.imshow(x, cmap=plt.cm.gray, interpolation='nearest')
    plt.show()
    print('Saving the checkerboard image in the Images folder as Checkerboard('+str(n*2)+').png ....')
    fig.savefig('Images/Checkerboard('+str(n*2)+').png')
    return plt.show()
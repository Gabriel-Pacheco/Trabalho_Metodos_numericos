import scipy
import scipy.linalg
import scipy.sparse
import scipy.sparse.linalg
import numpy as np

def showImage(X, Y, T, x, y):
    import matplotlib;
    matplotlib.use('Qt4Agg')
    import matplotlib.pylab as plt
    from mpl_toolkits.mplot3d import Axes3D
    from matplotlib import cm
    from matplotlib.ticker import LinearLocator, FormatStrFormatter
    import numpy as np

    fig = plt.figure()
    ax = fig.gca(projection='3d')
    surf = ax.plot_surface(X, Y, T, rstride=1, cstride=1, cmap=cm.coolwarm,
                           linewidth=0, antialiased=False)
    ax.set_zlim(0, 110)

    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('T [$^o$C]')
    ax.set_xticks(x)
    ax.set_yticks(y)

    fig.colorbar(surf, shrink=0.5, aspect=5)
    plt.show()

def main():
   pass

if __name__=="__main__":
    main()
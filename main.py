'''
Trabalho 1 - Algorítmos numéricos

Por: Filipe Mai, Gabriel Pacheco e Lucas Tersari
'''

import scipy
import scipy.linalg
import scipy.sparse
import scipy.sparse.linalg
import numpy as np

def saveMatrixExcel(matrix, local): # o local deve ser o local onde vc deseja salvar junto com o nome que vc deseja para o arquivo. Antes do 'C:...' deve ter a letra 'r', Ex: r'C:\Users\patri\Desktop\TrabAlg.xlsx'
    import pandas as pd
    matrix=matrix.toarray()
    df=pd.DataFrame(matrix)
    df.to_csv(local, sheet_name="df")

def showImage(theta):
   import matplotlib.pylab as plt
   from matplotlib import cm
   from matplotlib.ticker import LinearLocator, FormatStrFormatter

   xmax = 1
   ymax = 2
   
   Nx = 12
   h=xmax/Nx
   Ny = int(ymax/h)
   # surfaceplot:
   x = np.linspace(0, xmax, Nx + 1)
   y = np.linspace(0, ymax, Ny + 1)
   X, Y = np.meshgrid(x, y)

   W = np.resize(theta,new_shape=(25, 13))
   
   # set the imposed boudary values
   W[-1,:] = 1
   W[0,:] = 1
   W[:,0] = 1
   W[:,-1] = 1
   
   fig = plt.figure()
   ax = fig.gca(projection='3d')
   surf = ax.plot_surface(X, Y, W, rstride=1, cstride=1, cmap=cm.coolwarm,
                        linewidth=0, antialiased=False)

   ax.zaxis.set_major_locator(LinearLocator(10))
   ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
   
   ax.set_zlim(0, 6)
   ax.set_xlabel('x')
   ax.set_ylabel('y')
   ax.set_zlabel('W (N)')
   
   nx=4
   xticks=np.linspace(0.0,xmax,Nx)
   ax.set_xticks(xticks)
   
   ny=8
   yticks=np.linspace(0.0,ymax,Ny)
   ax.set_yticks(yticks)

   fig.colorbar(surf, shrink=0.5, aspect=5)

   # Plot 2D
   plt.figure()
   plt.pcolormesh(X, Y, W)
   plt.colorbar()
   
   plt.show()

def createMatrix(n):
    gratterDiagonal = np.ones(n)

    # Creating the diagonals
    d0 = 20*gratterDiagonal
    d1 = gratterDiagonal[0:-1] * (-8)
    d2 = gratterDiagonal[0:-2]
    d11 = gratterDiagonal[0:-11] * 2
    d12 = gratterDiagonal[0:-12] * (-8)
    d13 = gratterDiagonal[0:-13] * 2
    d24 = gratterDiagonal[0:-24]

    # Fixing each diagonal
    d0[0]=18
    d0[11]=18
    d0[84]=18
    d0[95]=18

    for i in range(1,11):
     d0[i] = 19 # em cima
     d0[i+84] = 19 # em baixo

    for i in range(1,7):
     d0[i*12] = 19 # esquerda
     d0[i*12+11] = 19 # direita

    for i in range(1, 8):
     d1[i*12-1] = 0
     d2[(i-1)*12+11-1] = 0
     d2[(i-1)*12+11] = 0
     d11[i*12] = 0
     d13[i*11] = 0
    d11[0]=0

    d24 = np.ones(len(d24))
    for i in range(1,13):
        d24[-i-12]=0  
        d24[-i]=0        
        
    print(len(d24))

    # Creating matrix A
    A = scipy.sparse.diags([d0, d1, d2,d11, d12, d13, d24, d1, d2, d11, d12, d13, d24 ],[0,1,2,11,12,13,24,-1,-2,-11,-12,-13,-24])

    return A

def Solving(A,b):
    return scipy.sparse.linalg.spsolve(A,b)

def main():
   n = 96
   b = np.ones(n,dtype=float) # solution
   A = createMatrix(n)

   print(A.toarray())

   sol = Solving(A,b)
   print(sol)

   showImage(sol)

if __name__=="__main__":
    main()
'''
Trabalho 1 - Algorítmos numéricos

Por: Filipe Mai, Gabriel Pacheco e Lucas Tersari
'''

import scipy
import scipy.linalg
import scipy.sparse
import scipy.sparse.linalg
import numpy as np
import matplotlib.pylab as plt

def saveMatrixExcel(matrix, local): # o local deve ser o local onde vc deseja salvar junto com o nome que vc deseja para o arquivo. Antes do 'C:...' deve ter a letra 'r', Ex: r'C:\Users\patri\Desktop\TrabAlg.xlsx'
    import pandas as pd
    df=pd.DataFrame(matrix)
    df.to_excel(local, sheet_name="df")

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

   fig = plt.figure()
   ax = fig.gca(projection='3d')
   surf = ax.plot_surface(X, Y, W, rstride=1, cstride=1, cmap=cm.coolwarm,
                        linewidth=0, antialiased=False)

   ax.zaxis.set_major_locator(LinearLocator(10))
   ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
   
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

def LinColPlaca_NumNohMatriz(NumNoh, NCols):
    #Placa começa em [1,1] e vair até [NLins,NCols]
    #NumNoh vai de 1 até NLins * NCols
    Lin = ((NumNoh-1)// NCols) + 1
    Col = ((NumNoh-1) % NCols) + 1
    return(Lin,Col)

def LinhaM_LinColPlaca(Lin, Col, NCols):
    #Placa começa em [0,0] e vair até [NLins-1,NCols-1]
    #NumNoh vai de 0 até (NLins * NCols - 1)
    NumNoh = NCols * Lin + (Col)
    return(NumNoh)

def createMatrix(n, NLinsPlaca, NColsPlaca):
    Matriz = np.zeros((n, n))

    #======== agora vamos fazer o canto noroeste (vermelho superior esquerda)=======
    stencil = np.array( [[0 , 0,  0,   0 , 0], 
                         [0 , 0 , 0  , 0 , 0],
                         [0 ,0 , 18 ,-8 , 1],
                         [0 , 0 , -8,  2,  0],
                         [0 , 0 , 1 ,  0,  0]])
    LinhaM = 0
    for dLin in range( 0, 3):
        LinVizPlaca =  dLin
        for dCol in range (0,3):
            ColVizPlaca =  dCol
            ColunaViz = LinhaM + (dLin * NColsPlaca) + dCol
            Matriz [LinhaM, ColunaViz] = stencil[2+dLin,2+dCol]

    #======== agora vamos fazer o ponto à direita do canto NW  =======
    stencil = np.array( [[0 , 0,  0, 0 , 0], 
                         [0 , 0 , 0  , 0 , 0],
                         [0 ,-8 , 19 , -8 , 1],
                         [0 , 2 , -8,  2,  0],
                         [0 , 0 , 1 ,  0,  0]])
    LinhaM = 1
    for dLin in range( 0, 3):
        LinVizPlaca =  dLin
        for dCol in range (-1,3):
            ColVizPlaca =  dCol
            ColunaViz = LinhaM + (dLin * NColsPlaca) + dCol
            Matriz [LinhaM, ColunaViz] = stencil[2+dLin,2+dCol]

    #======== agora vamos fazer o canto nordeste (vermelho superior direita)  =======
    stencil = np.array( [[0 , 0,  0,   0 , 0], 
                         [0 , 0 , 0  , 0 , 0],
                         [1 ,-8 , 18 , 0 , 0],
                         [0 , 2 , -8,  0,  0],
                         [0 , 0 , 1 ,  0,  0]])
    LinhaM = 11
    for dLin in range( 0, 3):
        LinVizPlaca =  dLin
        for dCol in range (-2,1):
            ColVizPlaca =  dCol
            ColunaViz = LinhaM + (dLin * NColsPlaca) + dCol
            Matriz [LinhaM, ColunaViz] = stencil[2+dLin,2+dCol]

     #======== agora vamos fazer borda norte da placa  =======
    stencil = np.array(  [[0 , 0,  0,   0 , 0], 
                          [0 , 0 , 0  , 0 , 0],
                          [1 ,-8 , 19 , -8 ,1],
                          [0 , 2 , -8,  2,  0],
                          [0 , 0 , 1 ,  0,  0]])
    for LinhaM in range (2, 11):
        for dLin in range( 0, 3):
            LinVizPlaca =  dLin
            for dCol in range (-2,3):
                ColVizPlaca =  dCol
                ColunaViz = LinhaM + (dLin * NColsPlaca) + dCol
                Matriz [LinhaM, ColunaViz] = stencil[2+dLin,2+dCol]

    #======== agora vamos fazer no miolo da placa  =======
    stencil = np.array( [[0 , 0,  1,   0 , 0], 
                         [0 , 2 ,-8  , 2 , 0],
                         [1 ,-8 , 20 ,-8 , 1],
                         [0 , 2 , -8,  2,  0],
                         [0 , 0 , 1 ,  0,  0]])
    
    LinhaM = 2 * NColsPlaca + 1
    cont=0
    print("Comeca a linhas:")
    for LinhaInteriorPlaca in range (2, NLinsPlaca-2):
        #os pontos interiores vao da 3a até antepenultima linha
        for ColunaInteriorPlaca in range (2, NColsPlaca-2):
            #... e da 3a até a antepenultima coluna
            LinhaM = LinhaM + 1
            if cont == 8:
                LinhaM = (LinhaM) + 4
                cont = 0
            cont = cont+1
            print(LinhaM)
            for dLin in range( -2, 3):
                for dCol in range (-2, 3):
                    ColunaViz = LinhaM + (dLin * NColsPlaca) + dCol
                    Matriz [LinhaM, ColunaViz] = stencil[2+dLin,2+dCol]
    
     #======== agora vamos fazer o ponto abaixo do canto NW  =======
    stencil = np.array( [[0 , 0,  0,   0 , 0], 
                         [0 , 0 ,-8  , 2 , 0],
                         [0 , 0 , 19 ,-8 , 1],
                         [0 , 0 ,-8,   2,  0],
                         [0 , 0 , 1 ,  0,  0]])
    LinhaM = 12
    for dLin in range( -1, 3):
        LinVizPlaca = dLin
        for dCol in range (0, 3):
            ColVizPlaca =  dCol
            ColunaViz = LinhaM + (dLin * NColsPlaca) + dCol
            Matriz [LinhaM, ColunaViz] = stencil[2+dLin,2+dCol]
   
     #======== agora vamos fazer borda oeste da placa  =======
    stencil = np.array(  [[0 , 0,  1,   0 , 0], 
                          [0 , 0 , -8  ,2 , 0],
                          [0 ,0 , 19 , -8 , 1],
                          [0 , 0 , -8,  2,  0],
                          [0 , 0 , 1 ,  0,  0]])
    for LinhaM in range (24, 61, 12):
        for dLin in range( -2, 3):
            LinVizPlaca =  dLin
            for dCol in range (0, 3):
                ColVizPlaca =  dCol
                ColunaViz = LinhaM + (dLin * NColsPlaca) + dCol
                Matriz [LinhaM, ColunaViz] = stencil[2+dLin,2+dCol]
    
     #======== agora vamos fazer o ponto acima do vermelho inferior esquerda  =======
    stencil = np.array( [[0 , 0,  1,   0 , 0], 
                         [0 , 0 ,-8  , 2 , 0],
                         [0 , 0 , 19 ,-8 , 1],
                         [0 , 0 ,-8,   2,  0],
                         [0 , 0 , 0 ,  0,  0]])
    LinhaM = 72
    for dLin in range( -2, 2):
        LinVizPlaca =  dLin
        for dCol in range (0, 3):
            ColVizPlaca =  dCol
            ColunaViz = LinhaM + (dLin * NColsPlaca) + dCol
            Matriz [LinhaM, ColunaViz] = stencil[2+dLin,2+dCol]

     #======== agora vamos fazer o ponto vermelho inferior esquerda  =======
    stencil = np.array( [[0 , 0,  1,   0 , 0], 
                         [0 , 0 ,-8  , 2 , 0],
                         [0 , 0 , 18 ,-8 , 1],
                         [0 , 0 , 0,   0,  0],
                         [0 , 0 , 0 ,  0,  0]])
    LinhaM = 84
    for dLin in range(-2, 1):
        LinVizPlaca =  dLin
        for dCol in range (0, 3):
            ColVizPlaca =  dCol
            ColunaViz = LinhaM + (dLin * NColsPlaca) + dCol
            Matriz [LinhaM, ColunaViz] = stencil[2+dLin,2+dCol]

     #======== agora vamos fazer o ponto a direita do vermelho inferior esquerdo =======
    stencil = np.array( [[0 , 0,  1,   0 , 0], 
                         [0 , 2 ,-8  , 2 , 0],
                         [0 ,-8 , 19 ,-8 , 1],
                         [0 , 0 , 0,   0,  0],
                         [0 , 0 , 0 ,  0,  0]])
    LinhaM = 85
    for dLin in range(-2, 1):
        LinVizPlaca =  dLin
        for dCol in range (0, 3):
            ColVizPlaca =  dCol
            ColunaViz = LinhaM + (dLin * NColsPlaca) + dCol
            Matriz [LinhaM, ColunaViz] = stencil[2+dLin,2+dCol]

     #======== agora vamos fazer borda sul da placa (azul claro)  =======
    stencil = np.array(  [[0 , 0,  1,   0 , 0], 
                          [0 , 2 , -8  , 2 , 0],
                          [1 ,-8 , 19 , -8 ,1],
                          [0 , 0 , 0,  0,  0],
                          [0 , 0 , 0 ,  0,  0]])
    for LinhaM in range (86, 94):
        for dLin in range( -2, 1):
            LinVizPlaca =  dLin
            for dCol in range (-2,3):
                ColVizPlaca =  dCol
                ColunaViz = LinhaM + (dLin * NColsPlaca) + dCol
                Matriz [LinhaM, ColunaViz] = stencil[2+dLin,2+dCol]

     #======== agora vamos fazer o ponto vermelho inferior direito  =======
    stencil = np.array( [[0 , 0,  1,   0 , 0], 
                         [0 , 2 ,-8  , 0 , 0],
                         [1 , -8 , 18 ,0 , 0],
                         [0 , 0 , 0,   0,  0],
                         [0 , 0 , 0 ,  0,  0]])
    LinhaM = 95
    for dLin in range(-2, 1):
        LinVizPlaca =  dLin
        for dCol in range (-2, 1):
            ColVizPlaca =  dCol
            ColunaViz = LinhaM + (dLin * NColsPlaca) + dCol
            Matriz [LinhaM, ColunaViz] = stencil[2+dLin,2+dCol]

     #======== agora vamos fazer o ponto a esqueda do vermelho inferior direito =======
    stencil = np.array( [[0 , 0,  1,   0 , 0], 
                         [0 , 2 ,-8  , 2 , 0],
                         [1 ,-8 , 19 ,-8 , 0],
                         [0 , 0 , 0,   0,  0],
                         [0 , 0 , 0 ,  0,  0]])
    LinhaM = 94
    for dLin in range(-2, 1):
        LinVizPlaca =  dLin
        for dCol in range (-2, 2):
            ColVizPlaca =  dCol
            ColunaViz = LinhaM + (dLin * NColsPlaca) + dCol
            Matriz [LinhaM, ColunaViz] = stencil[2+dLin,2+dCol]

     #======== agora vamos fazer o ponto acima do vermelho inferior direito =======
    stencil = np.array( [[0 , 0,  1,   0 , 0], 
                         [0 , 2 ,-8  , 0 , 0],
                         [1 ,-8 , 19 ,0 , 0],
                         [0 , 2 , -8,   0,  0],
                         [0 , 0 , 0 ,  0,  0]])
    LinhaM = 83
    for dLin in range(-2, 2):
        LinVizPlaca =  dLin
        for dCol in range (-2, 1):
            ColVizPlaca =  dCol
            ColunaViz = LinhaM + (dLin * NColsPlaca) + dCol
            Matriz [LinhaM, ColunaViz] = stencil[2+dLin,2+dCol]

     #======== agora vamos fazer borda leste da placa (azul claro)  =======
    stencil = np.array(  [[0 , 0,  1,   0 , 0], 
                          [0 , 2 , -8 , 0 , 0],
                          [1 ,-8 , 19 , 0 , 0],
                          [0 , 2 , -8,  0,  0],
                          [0 , 0 , 1 ,  0,  0]])
    for LinhaM in range (35, 72, 12):
        for dLin in range( -2, 3):
            LinVizPlaca =  dLin
            for dCol in range (-2,1):
                ColVizPlaca =  dCol
                ColunaViz = LinhaM + (dLin * NColsPlaca) + dCol
                Matriz [LinhaM, ColunaViz] = stencil[2+dLin,2+dCol]

     #======== agora vamos fazer o ponto abaixo do vermelho superior direito =======
    stencil = np.array( [[0 , 0,  0,   0 , 0], 
                         [0 , 2 ,-8  , 0 , 0],
                         [1 ,-8 , 19 , 0 , 0],
                         [0 , 2 ,-8,   0,  0],
                         [0 , 0 , 1 ,  0,  0]])
    LinhaM = 23
    for dLin in range(-1, 3):
        LinVizPlaca =  dLin
        for dCol in range (-2, 1):
            ColVizPlaca =  dCol
            ColunaViz = LinhaM + (dLin * NColsPlaca) + dCol
            Matriz [LinhaM, ColunaViz] = stencil[2+dLin,2+dCol]

     #======== agora vamos fazer o ponto do lado do azul escuro superior esquerdo =======
    stencil = np.array(  [[0 , 0,  0,   0 , 0], 
                          [0 , 2 , -8 , 2 , 0],
                          [0 ,-8 , 20 , -8 , 1],
                          [0 , 2 , -8,  2,  0],
                          [0 , 0 , 1 ,  0,  0]])
    LinhaM = 13
    for dLin in range(-1, 3):
        LinVizPlaca =  dLin
        for dCol in range (-1, 3):
            ColVizPlaca =  dCol
            ColunaViz = LinhaM + (dLin * NColsPlaca) + dCol
            Matriz [LinhaM, ColunaViz] = stencil[2+dLin,2+dCol]

     #======== agora vamos fazer borda norte da placa (cinza claro)  =======
    stencil = np.array(  [[0 , 0,  0,   0 , 0], 
                          [0 , 2 , -8 , 2 , 0],
                          [1 ,-8 , 20 , -8 , 1],
                          [0 , 2 , -8,  2,  0],
                          [0 , 0 , 1 ,  0,  0]])
    for LinhaM in range (14, 22):
        for dLin in range( -1, 3):
            LinVizPlaca =  dLin
            for dCol in range (-2,3):
                ColVizPlaca =  dCol
                ColunaViz = LinhaM + (dLin * NColsPlaca) + dCol
                Matriz [LinhaM, ColunaViz] = stencil[2+dLin,2+dCol]

     #======== agora vamos fazer o ponto do lado do azul escuro superior direito =======
    stencil = np.array(  [[0 , 0,  0,   0 , 0], 
                          [0 , 2 , -8 , 2 , 0],
                          [1 ,-8 , 20 , -8 , 0],
                          [0 , 2 , -8,  2,  0],
                          [0 , 0 , 1 ,  0,  0]])
    LinhaM = 22
    for dLin in range(-1, 3):
        LinVizPlaca =  dLin
        for dCol in range (-2, 2):
            ColVizPlaca =  dCol
            ColunaViz = LinhaM + (dLin * NColsPlaca) + dCol
            Matriz [LinhaM, ColunaViz] = stencil[2+dLin,2+dCol]

     #======== agora vamos fazer borda leste da placa (cinza claro)  =======
    stencil = np.array(  [[0 , 0,  1,   0 , 0], 
                          [0 , 2 , -8 , 2 , 0],
                          [1 ,-8 , 20 , -8 , 0],
                          [0 , 2 , -8,  2,  0],
                          [0 , 0 , 1 ,  0,  0]])
    for LinhaM in range (34, 71, 12):
        for dLin in range( -2, 3):
            LinVizPlaca =  dLin
            for dCol in range (-2,2):
                ColVizPlaca =  dCol
                ColunaViz = LinhaM + (dLin * NColsPlaca) + dCol
                Matriz [LinhaM, ColunaViz] = stencil[2+dLin,2+dCol]

     #======== agora vamos fazer o ponto do lado do azul escuro inferior direito =======
    stencil = np.array(  [[0 , 0,  1,   0 , 0], 
                          [0 , 2 , -8 , 2 , 0],
                          [1 ,-8 , 20 , -8 , 0],
                          [0 , 2 , -8,  2,  0],
                          [0 , 0 , 0 ,  0,  0]])
    LinhaM = 82
    for dLin in range(-2, 2):
        LinVizPlaca =  dLin
        for dCol in range (-2, 2):
            ColVizPlaca =  dCol
            ColunaViz = LinhaM + (dLin * NColsPlaca) + dCol
            Matriz [LinhaM, ColunaViz] = stencil[2+dLin,2+dCol]


     #======== agora vamos fazer borda sul da placa (cinza claro)  =======
    stencil = np.array(  [[0 , 0,  1,   0 , 0], 
                          [0 , 2 , -8 , 2 , 0],
                          [1 ,-8 , 20 , -8 , 1],
                          [0 , 2 , -8,  2,  0],
                          [0 , 0 , 0 ,  0,  0]])
    for LinhaM in range (74, 82):
        for dLin in range( -2, 2):
            LinVizPlaca =  dLin
            for dCol in range (-2,3):
                ColVizPlaca =  dCol
                ColunaViz = LinhaM + (dLin * NColsPlaca) + dCol
                Matriz [LinhaM, ColunaViz] = stencil[2+dLin,2+dCol]

     #======== agora vamos fazer o ponto do lado do azul escuro inferior esquerdo =======
    stencil = np.array(  [[0 , 0,  1,   0 , 0], 
                          [0 , 2 , -8 , 2 , 0],
                          [0 ,-8 , 20 , -8 , 1],
                          [0 , 2 , -8,  2,  0],
                          [0 , 0 , 0 ,  0,  0]])
    LinhaM = 73
    for dLin in range(-2, 2):
        LinVizPlaca =  dLin
        for dCol in range (-1, 3):
            ColVizPlaca =  dCol
            ColunaViz = LinhaM + (dLin * NColsPlaca) + dCol
            Matriz [LinhaM, ColunaViz] = stencil[2+dLin,2+dCol]


     #======== agora vamos fazer borda oeste da placa (cinza claro)  =======
    stencil = np.array(  [[0 , 0,  1,   0 , 0], 
                          [0 , 2 , -8 , 2 , 0],
                          [0 ,-8 , 20 , -8 , 1],
                          [0 , 2 , -8,  2,  0],
                          [0 , 0 , 1 ,  0,  0]])
    for LinhaM in range (25, 62, 12):
        for dLin in range( -2, 3):
            LinVizPlaca =  dLin
            for dCol in range (-1,3):
                ColVizPlaca =  dCol
                ColunaViz = LinhaM + (dLin * NColsPlaca) + dCol
                Matriz [LinhaM, ColunaViz] = stencil[2+dLin,2+dCol]

    return Matriz

def Solving(A,b):
    return scipy.linalg.solve(A,b)


def main():
    # definindo numero de linhas e colunas da grade
    NLinsPlaca = 8
    NColsPlaca = 12
    # Set simulation parameters
    n = NLinsPlaca * NColsPlaca
    b = np.ones(n) #vetor-mae para o lado direito (RHS)

    A = createMatrix(n, NLinsPlaca, NColsPlaca)

    solucao = Solving(A, b)  

if __name__=="__main__":
    main()
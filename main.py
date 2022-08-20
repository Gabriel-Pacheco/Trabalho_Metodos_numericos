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
from matrizParaSolucao import createMatrixSimplesmenteApoiado, createMatrixEngastado

def saveMatrixExcel(matrix, local): # o local deve ser o local onde vc deseja salvar junto com o nome que vc deseja para o arquivo. Antes do 'C:...' deve ter a letra 'r', Ex: r'C:\Users\patri\Desktop\TrabAlg.xlsx'
    import pandas as pd
    df=pd.DataFrame(matrix)
    df.to_excel(local, sheet_name="df")

def showImage(theta, NumLinsPlaca, NumColsPlaca):
    from mpl_toolkits import mplot3d
    import matplotlib.pyplot as plt
    plt.style.use('seaborn-poster')

    x = np.arange(0.0, 1.0*NumLinsPlaca, 1.0)
    y = np.arange(0.0, 1.0*NumColsPlaca, 1.0)
    X, Y = np.meshgrid(x, y)

    #print(X)
    #print(Y)

    Z = np.zeros_like(X)
    ind = 0
    for lin in range (0,NumLinsPlaca):
        for col in range (0,NumColsPlaca):
            Z[col,lin] = theta[ind]
            ind+=1
        
    fig = plt.figure(figsize = (12,10))
    ax = plt.axes(projection='3d')

    surf = ax.plot_surface(X, Y, Z, cmap = plt.cm.cividis)

    # Set axes label
    ax.set_xlabel('x', labelpad=20)
    ax.set_ylabel('y', labelpad=20)
    ax.set_zlabel('z', labelpad=20)

    fig.colorbar(surf, shrink=0.5, aspect=8)
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

def Solving(A,b):
    return scipy.linalg.solve(A,b)

def main():
    # definindo numero de linhas e colunas da grade
    NLinsPlaca = 8
    NColsPlaca = 12
    # Set simulation parameters
    n = NLinsPlaca * NColsPlaca
    b = np.ones(n) #vetor-mae para o lado direito (RHS)

    Q1 = createMatrixSimplesmenteApoiado(n, NLinsPlaca, NColsPlaca)
    Q1 = -Q1 # Para o gráfico ficar invertido
    Q2 = createMatrixEngastado(n, NLinsPlaca, NColsPlaca)
    Q2 = -Q2 # Para o gráfico ficar invertido

    solucao1 = Solving(Q1, b)  
    solucao2 = Solving(Q2, b)  
    showImage(solucao1, NLinsPlaca, NColsPlaca)
    showImage(solucao2, NLinsPlaca, NColsPlaca)
if __name__=="__main__":
    main()
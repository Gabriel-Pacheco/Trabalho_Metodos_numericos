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

def main():
    stencil = np.array( [[0 , 0,  1,   0 , 0], 
                         [0 , 2 ,-8  , 2 , 0],
                         [1 ,-8 , 20 ,-8 , 1],
                         [0 , 2 , -8,  2,  0],
                         [0 , 0 , 1 ,  0,  0]])

    placa = np.ones((12, 16), dtype=float)
    placa[0,:] = -1
    placa[1,:] = 0
    placa[-1,:] = -1
    placa[-2,:] = 0
    placa[:,0] = -1
    placa[:,1] = 0
    placa[:, -1] = -1
    placa[:, -2] = 0

    for i_p in range(2, placa.shape[0]-2):
        for j_p in range(2, placa.shape[1]-2):
            for i_s in range(0, stencil.shape[0]):
                for j_s in range(0, stencil.shape[1]):
                    placa[i_p, j_p] += placa[i_p-2 + i_s,j_p-2 + j_s]*stencil[i_s, j_s]
             
    placa=np.delete(placa,(0,1,10,11),axis=0)
    placa=np.delete(placa,(0,1,14,15),axis=1)
    saveMatrixExcel(placa, r'C:\Users\patri\Desktop\RespJeito2.xlsx')

if __name__=='__main__':
    main()
'''
Trabalho 1 - Algorítmos numéricos

Por: Filipe Mai, Gabriel Pacheco e Lucas Tersari
'''

import scipy
import scipy.linalg
import scipy.sparse
import scipy.sparse.linalg
import numpy as np

def showImage(X, Y, Z, x, y):
    pass

def main():
   n = 96
   gratterDiagonal = np.ones(n)
   b = np.zeros(n) # solution
   
   # Creating the diagonals
   d0 = 20*gratterDiagonal
   d1 = gratterDiagonal[0:-1] * (-8)
   d2 = gratterDiagonal[0:-2]
   d11 = gratterDiagonal[0:-11] * 2
   d12 = gratterDiagonal[0:-12] * (-8)
   d13 = gratterDiagonal[0:-13] * 2
   d24 = gratterDiagonal[0:-24]

   # Fixing each diagonal ( reference "miolo" )
    # first 4 light gray on the left (26, 38, 50, 62)
   d1[24] = d1[36] = d1[48] = d1[60] = 0
    # first 4 light blue on the left (25, 37, 49, 61)
   d0[24] = d0[36] = d0[48] = d0[60] = 19
   d1[23] = d1[25] = d1[47] = d1[59] = 0
   d13[11] = d13[23] = d13[35] = d13[47] = 0
    # first 5 light gray on top (14, 15, 16, 17, 18)
   d2[11] = 0
    # first 4 light blue on top (3, 4, 5, 6)
   d0[2] = d0[3] = d0[4] = d0[5] = 19
    # first dark blue on top (2)
   d0[1] = 19
    # first dark blue on left (13)
   d0[12] = 19
   d2[10] = 0
    # red on top-left (1)
   d0[0] = 18
    # first 5 light gray on botton (74, 75, 76, 77, 78)
   d2[71] = 0
    # first 4 light blue on botton (87, 88, 89, 90)
   d0[86] = d0[87] = d0[88] = d0[89] = 19
    # first dark blue on botton (86)
   d0[85] = 19
   d2[83] = 0
    # secound dark blue on left (73)
   d0[72] = 19
   d1[71] = 0
   d2[70] = 0
   d13[59] = 0
    # red on botton-left (85)
   d0[84] = 18
   d1[83] = 0
   d2[82] = 0
   d13[71] = 0
    # colum 12 (12, 24, 36, 48, 60, 72, 84, 96) for the lefts
   d11[0] = d11[12] = d11[0] = 0
   d24[] = 

   # Creating matrix A
   A = scipy.sparse.daigs([d0, d1, d2, ])

   print(d13.shape)

if __name__=="__main__":
    main()
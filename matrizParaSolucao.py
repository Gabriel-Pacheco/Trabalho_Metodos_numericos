def createMatrixSimplesmenteApoiado(n, NLinsPlaca, NColsPlaca):
    import numpy as np

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
    for LinhaInteriorPlaca in range (2, NLinsPlaca-2):
        #os pontos interiores vao da 3a até antepenultima linha
        for ColunaInteriorPlaca in range (2, NColsPlaca-2):
            #... e da 3a até a antepenultima coluna
            LinhaM = LinhaM + 1
            if cont == 8:
                LinhaM = (LinhaM) + 4
                cont = 0
            cont = cont+1
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




#######################################################
#######################################################
################# PARTE 2 DO TRABALHO #################
#######################################################
#######################################################


def createMatrixEngastado(n, NLinsPlaca, NColsPlaca):
    import numpy as np

    Matriz = np.zeros((n, n))

    #======== agora vamos fazer o canto noroeste (vermelho superior esquerda)=======
    stencil = np.array( [[0 , 0,  0,   0 , 0], 
                         [0 , 0 , 0  , 0 , 0],
                         [0 ,0 , 22 ,-8 , 1],
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
                         [0 ,-8 , 21 , -8 , 1],
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
                         [1 ,-8 , 22 , 0 , 0],
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
                          [1 ,-8 , 21 , -8 ,1],
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
    for LinhaInteriorPlaca in range (2, NLinsPlaca-2):
        #os pontos interiores vao da 3a até antepenultima linha
        for ColunaInteriorPlaca in range (2, NColsPlaca-2):
            #... e da 3a até a antepenultima coluna
            LinhaM = LinhaM + 1
            if cont == 8:
                LinhaM = (LinhaM) + 4
                cont = 0
            cont = cont+1
            for dLin in range( -2, 3):
                for dCol in range (-2, 3):
                    ColunaViz = LinhaM + (dLin * NColsPlaca) + dCol
                    Matriz [LinhaM, ColunaViz] = stencil[2+dLin,2+dCol]
    
     #======== agora vamos fazer o ponto abaixo do canto NW  =======
    stencil = np.array( [[0 , 0,  0,   0 , 0], 
                         [0 , 0 ,-8  , 2 , 0],
                         [0 , 0 , 21 ,-8 , 1],
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
                          [0 ,0 , 21 , -8 , 1],
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
                         [0 , 0 , 21 ,-8 , 1],
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
                         [0 , 0 , 22 ,-8 , 1],
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
                         [0 ,-8 , 21 ,-8 , 1],
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
                          [1 ,-8 , 21 , -8 ,1],
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
                         [1 , -8 , 22 ,0 , 0],
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
                         [1 ,-8 , 21 ,-8 , 0],
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
                         [1 ,-8 , 21 ,0 , 0],
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
                          [1 ,-8 , 21 , 0 , 0],
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
                         [1 ,-8 , 21 , 0 , 0],
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
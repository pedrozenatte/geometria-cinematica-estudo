# Exercise 3.17
#
# Four reference frames are shown in the robot workspace of Figure 3.23:
# the fixed frame {a}, the end-effector frame {b}, the camera frame {c},
# and the workpiece frame {d}.
#
# (a) Find T_ad and T_cd in terms of the dimensions given in the figure.
#
# (b) Find T_ab given that
#
#           [ 1  0  0  4 ]
#           [ 0  1  0  0 ]
# T_bc =    [ 0  0  1  0 ]
#           [ 0  0  0  1 ]

import numpy as np

T_ad = np.array([
    [1, 0, 0, -1],
    [0, 1, 0, 1],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
])

T_cd = np.array([
    [0, 1, 0, 0],
    [1, 0, 0, 0],
    [0, 0, -1, 2],
    [0, 0, 0, 1]
])

T_bc = np.array([
    [1, 0, 0, 4],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
])

def muda_coordenada_matriz(matriz: np.ndarray):
    """
    Função responsável por calcular a inversão de coordenada de uma matriz, T_xy para T_yx.
    """

    R_transposta = matriz[:3, :3].T
    translacao = matriz[:3, -1].reshape(3, 1)

    translacao_nova = -R_transposta @ translacao
    linha_homogenea = np.array([[0, 0, 0, 1]])

    # Vamos juntar as matrizes
    m = np.hstack((R_transposta, translacao_nova))
    T = np.vstack((m, linha_homogenea))

    return T



if __name__ == "__main__":
    T_dc = muda_coordenada_matriz(T_cd)
    T_ac = T_ad @ T_dc
    T_cb = muda_coordenada_matriz(T_bc)
    T_ab = T_ac @ T_cb
    print(T_ab)
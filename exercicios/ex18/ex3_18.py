# Exercise 3.18
#
# Consider a robot arm mounted on a spacecraft as shown in Figure 3.24, in
# which frames are attached to the Earth {e}, a satellite {s}, the spacecraft
# {a}, and the robot arm {r}, respectively.
#
# (a) Given T_ea, T_ar, and T_es, find T_rs.
#
# (b) Suppose that the frame {s} origin as seen from {e} is (1, 1, 1) and that
#
#          [ -1  0   0  1 ]
#          [  0  1   0  1 ]
# T_er =   [  0  0  -1  1 ]
#          [  0  0   0  1 ]
#
# Write down the coordinates of the frame {s} origin as seen from frame {r}.

import numpy as np

T_re = np.array([
    [-1, 0, 0, 1],
    [0, 1, 0, 1],
    [0, 0, -1, 1],
    [0, 0, 0, 1]
])

origem_S_em_E = np.array([
    [1],
    [1],
    [1],
    [1] # Coordenada homogênea
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
    T_er = muda_coordenada_matriz(T_re)
    origem_S_em_R = T_er @ origem_S_em_E

    print(origem_S_em_R)
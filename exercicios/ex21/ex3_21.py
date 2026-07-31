# Exercise 3.21
#
# The space station of Figure 3.27 moves in circular orbit around the Earth,
# and at the same time rotates about an axis always pointing toward the North
# Star. Owing to an instrument malfunction, a spacecraft heading toward the
# space station is unable to locate the docking port. An Earth-based ground
# station sends the following information to the spacecraft:
#
#          [ 0  -1   0  -100 ]
#          [ 1   0   0   300 ]
# T_ab =   [ 0   0   1   500 ]
#          [ 0   0   0     1 ]
#
#          [   0 ]
# p_a =    [ 800 ]
#          [   0 ]
#
# where p_a is the vector p expressed in {a}-frame coordinates.
#
# (a) From the given information, find r_b, the vector r expressed in
#     {b}-frame coordinates.
#
# (b) Determine T_bc at the instant shown in the figure. Assume here that the
#     ŷ- and ẑ-axes of the {a} and {c} frames are coplanar with the docking
#     port.


import numpy as np

T_ab = np.array([
    [0, -1, 0, -100],
    [1, 0, 0, 300], 
    [0, 0, 1, 500],
    [0, 0, 0, 1]
])

p_ab = np.array([
    [-100],
    [300],
    [500],
])

p_a = np.array([
    [0],
    [800],
    [0]
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
    ### Item A)
    r_a = p_a - p_ab

    # Acrescentando a coordenada homogênea para fazer os cálculos
    r_a = np.vstack((r_a, 1))

    r_b = muda_coordenada_matriz(T_ab) @ r_a

    print(f"Item a) \n{r_b}")

    ### Item B)
    T_ac = np.array([
        [1, 0, 0, 0],
        [0, np.cos(np.deg2rad(30)), -np.cos(np.deg2rad(60)), 800],
        [0, np.sin(np.deg2rad(30)), np.sin(np.deg2rad(60)), 0],
        [0, 0, 0, 1]
    ])

    T_bc = muda_coordenada_matriz(T_ab) @ T_ac
    print(f"Item b) \n{T_bc}")
# Exercise 3.2
# Let p be a point whose coordinates are p = (1/√3, -1/√6, 1/√2) with
# respect to the fixed frame x̂-ŷ-ẑ. Suppose that p is rotated about the fixed-
# frame x̂-axis by 30 degrees, then about the fixed-frame ŷ-axis by 135 degrees, and
# finally about the fixed-frame ẑ-axis by -120 degrees. Denote the coordinates of
# this newly rotated point by p'.
#
# (a) What are the coordinates p'?
# (b) Find the rotation matrix R such that p' = Rp for the p' you obtained in
#     (a).

import numpy as np

# Ponto P
P = np.array([
    1 / np.sqrt(3),
    -1 / np.sqrt(6),
    1 / np.sqrt(2)
])


# Função para rotacionar em torno do eixo X.
def rot_x(angulo: float, ponto: np.ndarray) -> np.ndarray:
    """
    Função que rotaciona um ponto/vetor em torno do eixo X. 

    angulo: É o ângulo de rotação no sentido positivo do círculo trigonométrico. 
    ponto: É o ponto ou vetor a ser rotacionado
    """

    # Convertendo o ângulo para radianos
    angulo = np.deg2rad(angulo)

    R_x = np.array([
        [1, 0, 0],
        [0, np.cos(angulo), -np.sin(angulo)],
        [0, np.sin(angulo), np.cos(angulo)]
    ])

    p_linha = R_x @ ponto

    return p_linha

# Função para rotacionar em torno do eixo X.
def rot_z(angulo: float, ponto: np.ndarray) -> np.ndarray:
    """
    Função que rotaciona um ponto/vetor em torno do eixo Z. 

    angulo: É o ângulo de rotação no sentido positivo do círculo trigonométrico. 
    ponto: É o ponto ou vetor a ser rotacionado
    """

    # Convertendo o ângulo para radianos
    angulo = np.deg2rad(angulo)

    R_z = np.array([
        [np.cos(angulo), -np.sin(angulo), 0],
        [np.sin(angulo), np.cos(angulo), 0],
        [0, 0, 1]
    ])

    p_linha = R_z @ ponto

    return p_linha


if __name__ == "__main__":
    p_rot_x = rot_x(30, P)
    p_rot_z = rot_z(15, p_rot_x)

    R_x = np.array([
        [1, 0, 0],
        [0, np.cos(np.deg2rad(30)), -np.sin(np.deg2rad(30))],
        [0, np.sin(np.deg2rad(30)), np.cos(np.deg2rad(30))]
    ])

    R_z = np.array([
        [np.cos(np.deg2rad(15)), -np.sin(np.deg2rad(15)), 0],
        [np.sin(np.deg2rad(15)), np.cos(np.deg2rad(15)), 0],
        [0, 0, 1]
    ])

    R = R_z @ R_x

    print(f"Valor de P ao rotacionar em torno de x: {p_rot_x}")
    print(f"Valor de P ao rotacionar em torno de z: {p_rot_z}")
    print()
    print(f"Matriz de rotação:\n {R}")
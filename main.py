from scipy.integrate import dblquad


def e_01_j(x_e, x_j_e, h_x_e):
    return (h_x_e ** 3 - 3 * h_x_e * (x_e - x_j_e) ** 2 + 2 * (x_e - x_j_e) ** 3) / h_x_e ** 3


def e_02_j(x_e, x_j_e, h_x_e):
    return (3 * h_x_e * (x_e - x_j_e) ** 2 - 2 * (x_e - x_j_e) ** 3) / h_x_e ** 3


def e_11_j(x_e, x_j_e, h_x_e):
    return (h_x_e ** 2 * (x_e - x_j_e) - 2 * h_x_e * (x_e - x_j_e) ** 2 + (x_e - x_j_e) ** 3) / h_x_e ** 2


def e_12_j(x_e, x_j_e, h_x_e):
    return (- h_x_e * (x_e - x_j_e) ** 2 + (x_e - x_j_e) ** 3) / h_x_e ** 2


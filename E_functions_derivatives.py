def e_01_der_1(x_e, x_j_e, h_x_e):
    return (6 * h_x_e * (x_e - x_j_e)+6 * (x_e - x_j_e) ^ 2) / (h_x_e ^ 3)


def e_01_der_2(x_e, x_j_e, h_x_e):
    return (-6 * h_x_e + 12 * (x_e - x_j_e)) / (h_x_e ^ 3)


def e_02_der_1(x_e, x_j_e, h_x_e):
    return (6 * h_x_e * (x_e - x_j_e) - 6 * (x_e - x_j_e) ^ 2) / (h_x_e ^ 3)


Необходимо заполнить первыми и вторыми производными функций фи
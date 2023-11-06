from E_functions import e_01, e_02, e_11, e_12


def phi_1(x_phi: float, y_phi: float, x_j_phi: float, y_i_phi: float, h_x_phi: float, h_y_phi: float):
    return e_01(x_phi, x_j_phi, h_x_phi) * e_01(y_phi, y_i_phi, h_y_phi)


def phi_2(x_phi: float, y_phi: float, x_j_phi: float, y_i_phi: float, h_x_phi: float, h_y_phi: float):
    return e_01(x_phi, x_j_phi, h_x_phi) * e_02(y_phi, y_i_phi, h_y_phi)


def phi_3(x_phi: float, y_phi: float, x_j_phi: float, y_i_phi: float, h_x_phi: float, h_y_phi: float):
    return e_02(x_phi, x_j_phi, h_x_phi) * e_01(y_phi, y_i_phi, h_y_phi)


def phi_4(x_phi: float, y_phi: float, x_j_phi: float, y_i_phi: float, h_x_phi: float, h_y_phi: float):
    return e_02(x_phi, x_j_phi, h_x_phi) * e_02(y_phi, y_i_phi, h_y_phi)


def phi_5(x_phi: float, y_phi: float, x_j_phi: float, y_i_phi: float, h_x_phi: float, h_y_phi: float):
    return e_11(x_phi, x_j_phi, h_x_phi) * e_01(y_phi, y_i_phi, h_y_phi)


def phi_6(x_phi: float, y_phi: float, x_j_phi: float, y_i_phi: float, h_x_phi: float, h_y_phi: float):
    return e_11(x_phi, x_j_phi, h_x_phi) * e_02(y_phi, y_i_phi, h_y_phi)


def phi_7(x_phi: float, y_phi: float, x_j_phi: float, y_i_phi: float, h_x_phi: float, h_y_phi: float):
    return e_12(x_phi, x_j_phi, h_x_phi) * e_01(y_phi, y_i_phi, h_y_phi)


def phi_8(x_phi: float, y_phi: float, x_j_phi: float, y_i_phi: float, h_x_phi: float, h_y_phi: float):
    return e_12(x_phi, x_j_phi, h_x_phi) * e_02(y_phi, y_i_phi, h_y_phi)


def phi_9(x_phi: float, y_phi: float, x_j_phi: float, y_i_phi: float, h_x_phi: float, h_y_phi: float):
    return e_01(x_phi, x_j_phi, h_x_phi) * e_11(y_phi, y_i_phi, h_y_phi)


def phi_10(x_phi: float, y_phi: float, x_j_phi: float, y_i_phi: float, h_x_phi: float, h_y_phi: float):
    return e_01(x_phi, x_j_phi, h_x_phi) * e_12(y_phi, y_i_phi, h_y_phi)


def phi_11(x_phi: float, y_phi: float, x_j_phi: float, y_i_phi: float, h_x_phi: float, h_y_phi: float):
    return e_02(x_phi, x_j_phi, h_x_phi) * e_11(y_phi, y_i_phi, h_y_phi)


def phi_12(x_phi: float, y_phi: float, x_j_phi: float, y_i_phi: float, h_x_phi: float, h_y_phi: float):
    return e_02(x_phi, x_j_phi, h_x_phi) * e_12(y_phi, y_i_phi, h_y_phi)

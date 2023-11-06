from Phi_functions import phi_1, phi_2, phi_3, phi_4, phi_5, phi_6, phi_7, phi_8, phi_9, phi_10, phi_11, phi_12

PHI_NUMB = {
    1: phi_1,
    2: phi_2,
    3: phi_3,
    4: phi_4,
    5: phi_5,
    6: phi_6,
    7: phi_7,
    8: phi_8,
    9: phi_9,
    10: phi_10,
    11: phi_11,
    12: phi_12,
}


def fw(
    f_1_fw: int,
    f_2_fw: int,
    x_fw: float,
    y_fw: float,
    x_j_fw: float,
    y_i_fw: float,
    h_x_fw: float,
    h_y_fw: float,
) -> float:
    args1 = x_fw, y_fw, x_j_fw, y_i_fw, h_x_fw, h_y_fw
    result = PHI_NUMB[f_1_fw](*args1) * PHI_NUMB[f_2_fw](*args1)
    return result
Необходимо собрать функцию, как в книге на стр. 228

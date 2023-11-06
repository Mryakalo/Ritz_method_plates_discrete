from scipy.integrate import dblquad
from FW import fw

x_j = 3.0
y_i = 4.0
h_x = 5.0
h_y = 6.0
Интеграл пока построен для тестов. Необходимо создать файл с функциями вычисления
интеграла (оператор А в книге на стр. 228)
и записать аккуратно выражения для всех коэффициентов СЛАУ. Потом решить СЛАУ
Integral = dblquad(lambda y, x: fw(1, 2, x, y, x_j, y_i, h_x, h_y), 1, 8, lambda y: 0, lambda y: 1)
print(Integral)



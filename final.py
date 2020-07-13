import matplotlib.pyplot as plt  # библиотека графиков
import scipy.constants as const  # библиотека констант
import numpy as np  # математическая библиотека
import scipy.special as sp


def сmtom():  # 1 centimeter -> 0.01 meter
    return 10 ** -2


def nctoc():
    return 10 ** -9


to_show_graph = False
to_print_values = False
iterations = 1000
N = iterations
precision = 10 ** -8  # for cases when value under root is < 0

xn = 6.0 * сmtom()
yn = 6.4 * сmtom()
k_value = 1 / (4 * const.pi * const.epsilon_0)
el_charge_q = 2 * nctoc()


def redx1(k):
    result = 3 + (k * 6) / N
    return result * сmtom()


def redy1():
    return 3 * сmtom()


def bluex2(k):
    result = 1 + (k * 10) / N
    return result * сmtom()


def bluey2(k):
    blue_x2 = bluex2(k)
    first_under_root_part = (5 * сmtom()) ** 2
    second_under_root_part = (blue_x2 - 6 * сmtom()) ** 2
    under_root_part = first_under_root_part - second_under_root_part
    if np.absolute(under_root_part) < precision:
        under_root_part = 0
    root_part = np.sqrt(under_root_part)
    result = (4 * сmtom()) + root_part
    return result


red_x1_array = []
red_y1_array = []
blue_x2_array = []
blue_y2_array = []

for it in range(0, N + 1):
    new_red_x1 = redx1(it)
    new_red_y1 = redy1()
    new_blue_x2 = bluex2(it)
    new_blue_y2 = bluey2(it)
    red_x1_array.append(new_red_x1)
    red_y1_array.append(new_red_y1)
    blue_x2_array.append(new_blue_x2)
    blue_y2_array.append(new_blue_y2)

if to_print_values:
    print("all the red_x1 values:")
    print(red_x1_array)
    print("all the red_y1 values:")
    print(red_y1_array)

if to_print_values:
    print("all the blue_x2 values:")
    print(blue_x2_array)
    print("all the blue_y2 values:")
    print(blue_y2_array)

plt.scatter(red_x1_array, red_y1_array, c="red")
plt.scatter(blue_x2_array, blue_y2_array, c="blue")

if to_show_graph:
    plt.show()
else:
    print("not showing graph")


def redr1(k):
    red_x1 = red_x1_array[k]
    red_y1 = red_y1_array[k]
    first_under_root = (xn - red_x1) ** 2
    second_under_root = (yn - red_y1) ** 2
    under_root = first_under_root + second_under_root
    if np.absolute(under_root) < precision:
        under_root = 0
    result = np.sqrt(under_root)
    return result


def reda1(k):
    red_x1 = red_x1_array[k]
    red_y1 = red_y1_array[k]
    first_part = xn - red_x1
    second_part = yn - red_y1
    fraction = first_part / second_part
    return np.arctan(fraction)


def bluer2(k):
    blue_x2 = blue_x2_array[k]
    blue_y2 = blue_y2_array[k]
    first_under_root = (xn - blue_x2) ** 2
    second_under_root = (yn - blue_y2) ** 2
    under_root = first_under_root + second_under_root
    if np.absolute(under_root) < precision:
        under_root = 0
    result = np.sqrt(under_root)
    return result


def bluea2(k):
    blue_x2 = blue_x2_array[k]
    red_y1 = red_y1_array[k]
    blue_y2 = blue_y2_array[k]
    first_part = xn - blue_x2
    second_part = red_y1 - yn
    fraction = first_part / second_part
    return np.arctan(fraction)


red_r1_array = []
red_a1_array = []
blue_r2_array = []
blue_a2_array = []
for it in range(0, N + 1):
    red_r1 = redr1(it)
    blue_r2 = bluer2(it)
    red_r1_array.append(red_r1)
    blue_r2_array.append(blue_r2)
    red_a1 = reda1(it)
    blue_a2 = bluea2(it)
    red_a1_array.append(red_a1)
    blue_a2_array.append(blue_a2)

if to_print_values:
    print("all the red_r1 values:")
    print(red_r1_array)
    print("all the red_a1 values:")
    print(red_a1_array)

if to_print_values:
    print("all the blue_r2 values:")
    print(blue_r2_array)
    print("all the blue_a2 values:")
    print(blue_a2_array)


def RedEX1(k):
    result = el_charge_q * k_value
    result = result / (red_r1_array[k] ** 2)
    result = result * np.sin(red_a1_array[k])
    return result


def RedEY1(k):
    result = el_charge_q * k_value
    result = result / (red_r1_array[k] ** 2)
    result = result * np.cos(red_a1_array[k])
    return result


def BlueEX2(k):
    result = el_charge_q * k_value
    result = result / (blue_r2_array[k] ** 2)
    result = result * np.sin(blue_a2_array[k])
    return result


def BlueEY2(k):
    result = (-1) * el_charge_q * k_value
    result = result / (blue_r2_array[k] ** 2)
    result = result * np.cos(blue_a2_array[k])
    return result


red_ex1_array = []
red_ey1_array = []
blue_ex2_array = []
blue_ey2_array = []
for it in range(0, N + 1):
    red_ex1 = RedEX1(it)
    red_ey1 = RedEY1(it)
    red_ex1_array.append(red_ex1)
    red_ey1_array.append(red_ey1)
    blue_ex2 = BlueEX2(it)
    blue_ey2 = BlueEY2(it)
    blue_ex2_array.append(blue_ex2)
    blue_ey2_array.append(blue_ey2)

if to_print_values:
    print("all the red_ex1 values:")
    print(red_ex1_array)
    print("all the red_ey1 values:")
    print(red_ey1_array)

if to_print_values:
    print("all the blue_ex2 values:")
    print(blue_ex2_array)
    print("all the blue_ey2_values:")
    print(blue_ey2_array)

red_final_ex1 = 0
red_final_ey1 = 0
blue_final_ex2 = 0
blue_final_ey2 = 0

for it in range(0, N + 1):
    red_final_ex1 += red_ex1_array[it]
for it in range(0, N + 1):
    red_final_ey1 += red_ey1_array[it]
for it in range(0, N + 1):
    blue_final_ex2 += blue_ex2_array[it]
for it in range(0, N + 1):
    blue_final_ey2 += blue_ey2_array[it]

print("red_final_ex1 value:", red_final_ex1)
print("red_final_ey1 value:", red_final_ey1)
print("blue_final_ex2 value:", blue_final_ex2)
print("blue_final_ey2 values:", blue_final_ey2)

final_x = red_final_ex1 + blue_final_ex2
final_y = red_final_ey1 + blue_final_ey2
print("final_x =", final_x)
print("final_y =", final_y)

final_e = np.sqrt((final_x ** 2) + (final_y ** 2))
print("result: E=", final_e)
print("result is k*10^6, find k")
answer = final_e / 1000
answer = int(round(answer))
print("answer k:", answer)

import math
print("ax2 + bx + c = 0")
input_a = input("Введите число a: ")
a = int(input_a)
input_b = input("Введите число b: ")
b = int(input_b)
input_c = input("Введите число b: ")
c = int(input_c)
D = (pow(b, 2) - 4 * (a * c))
D_sqrt = (D ** 0.5)
x1 = f"(-b + {D_sqrt} / 2 * a)"
x2 = f"(-b - {D_sqrt} / 2 * a)"
print("x1 =", x1, "x2 =", x2)

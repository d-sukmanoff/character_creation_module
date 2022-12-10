from math import sqrt

message = ('Добро пожаловать в самую лучшую программу для вычисления '
           'квадратного корня из заданного числа')
print(message)


def calculatesqrt(number) -> float:
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(your_number):
    if your_number <= 0:
        return
    print(f'Мы вычислили квадратный '
          f'корень из введённого вами числа. '
          f'Это будет: {calculatesqrt(your_number)}')


print(message)
calc(25.5)

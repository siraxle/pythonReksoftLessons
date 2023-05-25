# Звездный треугольник
def draw_triangle():
    n = 10
    for i in range(1, n + 1):
        for j in range(0, i):
            print('*', end='')
        print()


draw_triangle()


# Конвертер километров
def convert_to_miles(km):
    return km * 0.6214


print(convert_to_miles(10))


# Is Number Prime
def is_prime(number):
    if number > 0:
        if number == 1:
            return False
        for x in range(2, number):
            if number % x == 0:
                return False
        return True
    else:
        print("INVALID DATA")


print(is_prime(11))


# Next Prime
def get_next_prime(num):
    while True:
        if is_prime(num):
            return num
        else:
            num = num + 1


print(get_next_prime(90))

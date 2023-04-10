print("Задача про время и Колю")
hours = int(input("Сколько часов спит Тимофей: "))
minutesTimofey = int(input("Сколько минут спит Тимофей: "))
print("Тимофей обычно спит " + str(hours * 60 + minutesTimofey) + " минут")

print("============================")

print("Задача про время и Колю")
minutesKolya = int(input("Сколько минут спит Коля: "))
print("Коля спит " + str(minutesKolya // 60) + " часа(ов)")
print("и " + str(minutesKolya % 60) + " минут")

print("============================")

print("Вычисление площади треугольника по формуле Герона")
a = float(input("Введите a: "))
b = float(input("Введите b: "))
c = float(input("Введите c: "))
p = (a + b + c) / 2
S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
print("Площадь треугольника равна: " + str(S))

print("============================")

print("Определение високосного года")
year = int(input("Введите год: "))
if year >= 1900 and year <= 3000:
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print("Високосный")
    else:
        print("Обычный")

print("============================")

print("Рекомендованный сон")
A = int(input("Рекомендованно спать: "))
B = int(input("Не рекомендованно спать более: "))
H = int(input("Аня спит: "))
if H == A:
    print("Здоровье")
elif H > A:
    print("Пересып")
elif H < B:
    print("Недосып")


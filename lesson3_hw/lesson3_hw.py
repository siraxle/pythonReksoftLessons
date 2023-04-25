# Список делителей
i = int(input())
listOfNumbers1 = list()
if i > 0:
    for j in range(1, i + 1):
        if i % j == 0:
            listOfNumbers1.append(j)
    print(listOfNumbers1)
else:
    print("ERROR INPUT")

# Сумма двух
n = int(input())
listOfNumbers2 = list()
res = list()
if n >= 2:
    while n > 0:
        listOfNumbers2.append(int(input()))
        n = n - 1
    for k in range(0, len(listOfNumbers2) - 1):
        res.append(listOfNumbers2[k] + listOfNumbers2[k + 1])
    print(res)
else:
    print("n must be more or equals 2")

# Символы всех строк
nCount = int(input())
nStrings = list()
if nCount > 0:
    while nCount > 0:
        nStrings.extend(input())
        nCount -= 1
    print(nStrings)
else:
    print("INPUT ERROR")

# Удалите нечетные индексы
n2 = int(input())
nlist = list()
if n2 > 2:
    while n2 > 0:
        nlist.append(int(input()))
        n2 -= 1
else:
    print("n must be more then 2")
del nlist[1::2]
print(nlist)
# task_1
res = 0
while True:
    x = int(input())
    if x > 0:
        res = res + x
    else:
        break
print(res)

# task_2
y = int(input())
for i in range(1, 10):
    print(y * i)

# task_3
z = int(input())
result = 1
for i in range(2, z):
    if i % 2 == 0:
        result = result - i
    else:
        result = result + i
print(result)

# task_4
n = int(input())
i = 1
while i <= n:
    i = i + 1
    if n % i == 0:
        print(i)
        break

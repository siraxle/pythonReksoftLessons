# Task 1
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# first solution
res = []
for i in a:
    for j in b:
        if i == j:
            res.append(i)
            break
print(res)

# second solution
res2 = list(filter(lambda x: x in b, a))
print(res2)

# Task 2
# 1, 1, 2, 3, 5, 8, 13
st = input()
l = []
list(map(lambda x: l.append(x), st.split(',')))
print(l)
t = tuple(l)
print(t)

# Task 3
ar = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list(map(lambda y: print(y), filter(lambda x: x < 5, ar)))

# Task 4
ar2 = [1, 1, 2, 45, 3, 5, 8, 30, 13, 21, 34, 55, 89, 15]
res15 = []
list(map(lambda x: res15.append(x), filter(lambda x: x % 15 == 0, ar2)))
print(res15)
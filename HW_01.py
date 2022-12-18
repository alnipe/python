# Python. HW_01.
# Part_1

# 1) Создать переменную типа String
a = "Hello"
print(a, type(a))

# 2) Создать переменную типа Integer
b = 13
print(b, type(b))

# 3) Создать переменную типа Float
c = 3.14
print(c, type(c))

# 4) Создать переменную типа Bytes
d = b"Hello"
print(d, type(d))

# 5) Создать переменную типа List
e = ["red", "yellow", "green"]
print(e, type(e))

# 6) Создать переменную типа Tuple
f = (1, 2, 3)
print(f, type(f))

# 7) Создать переменную типа Set
g = set('hello')
print(g, type(g))

# 8. Создать переменную типа Frozen set
hh = frozenset('hello')
print(hh, type(hh))

# 9) Создать переменную типа Dict
i = {'age_1': 30, 'name': "Alex"}
print(i, type(i))

# 10) Вывести в консоль все вышеперечисленные переменные с добавлением типа данных.
#
# 11) Создать 2 переменные String, создать переменную в которой сканкатенируете эти переменные. Вывести в консоль.
j = "Home"
k = "work 01"
l = j + k
print(l)

# 12) Вывести в одну строку переменные типа String и Integer используя “,” (Запятую)
print(a, b, sep=',')

# 13) Вывести в одну строку переменные типа String и Integer используя “+” (Плюс)
print(a + str(b))

a = 19245301  # 2022
b = 4218520  # 2021
c = 271  # 2020
d = b-c
e = a-b
if d < e:
    print("e is greater")
if d > e:
    print("d is greater")
f = d/c
g = e/b
if f < g:
    print("The rate of new cases was greater in 2021.")
if f > g:
    print("The rate of new cases was greater in 2020.")


X = 0
Y = 1
bool(X)
bool(Y)
print("X:", bool(X))
print("Y:", bool(Y))
Z = bool(X) and bool(Y)
print("X and Y:", Z)

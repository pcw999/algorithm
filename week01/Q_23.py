n = int(input())
n_1 = 0
n_2 = 0
n_3 = 0

if n < 10 :
    n_1 = n
elif n < 100 :
    n_2 = n // 10
    n_1 = n % 10
else :
    n_3 = n // 100
    n_2 = (n%100) // 10
    n_1 = n % 10

print(n_1, n_2, n_3)
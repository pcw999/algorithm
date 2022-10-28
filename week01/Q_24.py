import copy
row, col = map(int, input().split())
temp = []
squre = []

for i in range(col) :
    for j in range(row) :
        temp.append('O')

    squre.append(copy.deepcopy(temp))
    temp.clear()

print(squre)
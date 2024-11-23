def get_matrix(n,m,value):
    matrix = []
    for i in range(n):
        list1 = []
        matrix.append(list1)
        for j in range(m):
            list1.append(value)
    return matrix
result1 = get_matrix(4,5,7)
result2 = get_matrix(5,4,11)
result3 = get_matrix(2,3,0)

print(result1)
print(result2)
print(result3)

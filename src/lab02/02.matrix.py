def transpose(mat: list[list[float | int]]):
    an = [[] for _ in range(len(mat))]
    k = 0
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            an[k].append(mat[j][i])
        k+=1
    return an

print(transpose([[1,2,3],[4,5,6],[7,8,9]]))

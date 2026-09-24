from ..lib import testing

def min_max(nums: list[float | int]):
    if len(nums)==0:
        raise ValueError()
    else:
        return tuple([min(nums),max(nums)])

    
def unique_sorted(nums: list[float | int]):
    return sorted(set(nums))


def flatten(mat: list[list | tuple]):
    an = []
    for i in mat:
        if type(i)!=list and type(i)!=tuple:
            raise TypeError
        else: 
            an.extend(i)
    return an





test_minmax = [
    [3, -1, 5, 5, 0],
    [42],
    [-5, -2, -9],
    [],
    [1.5, 2, 2.0, -3.1]
]
test_unique_sorted=[
    [3, 1, 2, 1, 3],
    [],
    [-1, -1, 0, 2, 2],
    [1.0, 1, 2.5, 2.5, 0] ,
]
test_flatten=[
    [[1, 2], [3, 4]],
    [[1, 2], (3, 4, 5)],
    [[1], [], [2, 3]],
    [[1, 2], "ab"]
]

print()
print("MIN_MAX")
testing(min_max, test_minmax)
print()
print("UNIQUE_SORTED")
testing(unique_sorted, test_unique_sorted)
print()
print("FLATTEN")
testing(flatten,test_flatten)
print()
import numpy


def solution(arr):
    # Write your code here
    deciArray = []
    rslt = []

    for x in arr:
        deci = 0
        for y in x:
            deci += 2 ** y

        deciArray.append(deci)
    sortedArray = sorted(deciArray, reverse=True)

    for x in sortedArray:
        rslt.append(deciArray.index(x))

    return rslt


arr = [[0, 1, 2], [3, 1, 0]]
print(solution(arr))

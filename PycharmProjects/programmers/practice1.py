def lcs(x, y):
    i = len(x)
    j = len(y)
    result = []
    for k in range(i):
        try:
            z = result[k]
        except IndexError:
            result[k] = []  # 이전 계산 값 저장 공간
    for k in range(i):
        for l in range(j):
            print(k, l)
            if k == 0 or l == 0:
                result[k][l] = 0
            elif x[k - 1] == y[l - 1]:
                result[k][l] = result[k - 1][l - 1] + 1
            else:
                result[k][l] = max(result[k - 1][l], result[k][l - 1])

    return result[i][j]


lcs("ABCBDAB", "BDCABA")


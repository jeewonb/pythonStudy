def solution(nodeinfo):
    answer = [[]]
    preorder = []
    postorder = []
    left = []
    right = []
    pre = sorted(
        sorted(nodeinfo, key=lambda n: n[0], reverse=False),
        key=lambda n: n[1],
        reverse=True,
    )
    x = pre[0]
    y = pre[1]

    for i in range(len(pre)):
        if pre[i + 1][1] < pre[i][1] and pre[i + 1][0] > pre[i][0]:
            preorder.append(i)
            continue
        if pre[i + 1][1] == pre[i][1] and pre[i + 1][0] < pre[i][0]:
            preorder.append(i)
            continue

    print(pre)

    return answer


nodeinfo = [[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]]
solution(nodeinfo)

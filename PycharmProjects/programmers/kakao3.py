import numpy as np
import copy

k = 3
arrival = [1, 2, 12, 5, 6, 30, 32]
load = [15, 10, 10, 10, 10, 15, 10]


def solution(k, arrival, load):
    sortedArrival = np.argsort(np.argsort(arrival)).tolist()

    current = [0] * k
    total = [0] * k
    last = 0

    realLast = 0
    for i in range(len(sortedArrival)):
        ## 타겟마다 조회
        cnt = 0
        while i < len(sortedArrival):
            if cnt == k:
                print("dropped: ", arrival[target])
                last = realLast
                break

            if last > k - 1 and cnt < k:
                last = 0  ## 다시 처음부터

            target = sortedArrival.index(i)
            print("now -- : ", arrival[target])

            if current[last] <= arrival[target]:
                current[last] += arrival[target] + load[target] - 1
                total[last] += load[target]
                print("loaded: ", arrival[target], last, load[target])
                realLast = copy.copy(last)
                break
            else:
                cnt += 1
                last += 1

        if i == len(sortedArrival) - 1:
            break

    return total.index(max(total))


print(solution(k, arrival, load))


import string

s = "ZNMD"


def solution(s):
    # Write your code here
    track = []
    total = 0
    for i in range(len(s)):
        idx = list(string.ascii_uppercase).index(s[i])
        track.append(idx)

        if len(track) == 1:
            total += min(idx, 26 - idx)
            continue

        diff = abs(idx - list(string.ascii_uppercase).index(s[i - 1]))

        total += min(diff, 26 - diff)

    return total


print(solution(s))

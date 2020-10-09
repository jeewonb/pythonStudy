#test3.py

def solution(n):
    ans = 0

    while True:
        if n%2 == 0:
            n = n/2
            continue
        if n%2 == 1:
            n = (n-1)/2
            ans += 1
        if n == 0:
            break
    print(ans)
    return ans

solution(5)
solution(6)
solution(5000)
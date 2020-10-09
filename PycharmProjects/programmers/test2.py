def solution(nums):
    answer = 0
    half = len(nums)/2
    distinct = len(set(nums))
    if half > distinct :
        answer =  half
    else:
        answer = distinct
    return answer


solution([3,1,2,3])
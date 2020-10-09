# def solution(n):
#     answer = ''
#     if n % 2 == 0:
#         answer = '수박' * int(n/2)
#     else:
#         answer = '수박'*int(n/2-0.5) + '수'
#     return answer


# print(solution(4))


# def solution(n):
#     answer = ''
#     for a in range(0, n):
#         if a % 2 == 0:
#             answer += '수'
#         else:
#             answer += '박'
#    return answer

# 50000000000000

# def solution(n):
#     answer = 0

#     while True:
#         for a in range(0, 23000000):
#             if a ** 2 == n:
#                 answer = (a + 1) ** 2
#                 break
#             if a == 23000000:
#                 answer = -1
#         return answer


# print(solution(121))


# def solution(people, limit):
#     answer = 0
#     ##
#     cnt = 0
#     start = 0
#     end = len(people) - 1
#     people.sort()

#     while True:
#         if people[start] + people[end] <= limit:
#             cnt += 1
#             answer += 1
#             start += 1
#             end -= 1
#             print(1, start, end, answer)
#         if start == end:
#             start += 1
#             print(2, start, end, answer)
#             continue
#         if cnt * 2 + 1 == len(people):
#             print(3, start, end, answer)
#             break
#         if end == 0:
#             print(4, start, end, answer)
#             break
#         else:
#             cnt += 1
#             end -= 1
#             print(5, start, end, answer)

#     return len(people) - answer


# print(solution([70, 50, 80, 50], 100))

def solution(board):
    height = len(board)
    width = len(board[0])
    map1 = {}
    map2 = {}
    for i in range(0,width):
        for j in range(0, height):
            # if len(map) == 0:
            #     map = {(i,j) : board[i][j]}
            map1[(i, j)] = board[j][i]

    for i in range(0,height):
        for j in range(0, width):
            # if len(map) == 0:
            #     map = {(i,j) : board[i][j]}
            map2[(i, j)] = board[i][j]


    print(map1)
    print(map2)

solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]])
print("#############")
solution([[0,0,1,1],[1,1,1,1]])
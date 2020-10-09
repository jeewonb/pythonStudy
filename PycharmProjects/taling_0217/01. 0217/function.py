
# 함수 정의
def add(a, b):
    c = a + b
    return c

# 함수 호출

    result = add(10, 20) # 먼저 여기로 오고 10, 20을 가지고 위에 add 함수로 간다.
    print(result)

def func1():
    a = 1 #지역 변수: 그 지역에서만 접근 가능

#print(a)

num = 10 # 전역 변수: 모든 지역에서 접근 가능
            # read-only : 값을 수정할 수 없음... 다른 지역에서 수정 불

def func2():
    global num # 이걸 추가해야 함 !!!!
    num += 10
    print(num)




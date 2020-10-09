def solution(s):
    answer = 0
    testList = []
    for a in s:
        testList.append(a)
    print('list', testList)  
    while True:
        try:
            deleteFn(testList)
            
            if len(testList) == 0:
                print("answer: 1")
                break
            else:
                print("answer: 0")
                break
        except IndexError:
            return

    return answer

def deleteFn(a):
    for i in range(len(a)):  
        try:
            if a[i] == a[i+1]:
                print("same ", a[i], a[i+1])
                del a[i]
                del a[i]
                print("del result: ", a)
        except IndexError:
            return      
        
    return deleteFn(a)


# solution("baabaa")
solution("caca")
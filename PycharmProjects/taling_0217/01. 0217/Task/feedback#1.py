
phoneList = []
numOfData = 0


def inputData():
    while True:
        name = input("이름 입력: ")
        number = input("번호 입력: ")
        # 오.. 빈칸 입력 방지 기능까지 넣어주셨네요..! 좋은 아이디어 입니다.
        if name != "" and number != "":
            phoneList.append({"name": name, "number": number})
            global numOfData
            numOfData += 1
            return
        else:
            print("*" * 20)
            print("ERROR: 공백없이 입력하세요.")
            continue


def searchData():
    # 와 완벽합니다. 개발할 때 이러한 사소한 예외들을 잘 처리하는게 되게 어려운데
    # 정말 잘해주셨네요..!
    if numOfData < 1:
        print("ERROR: 연락처를 먼저 등록해주세요.")
    else:
        name = input("찾을 이름 입력: ")
    # 이 아래 부분은 제가 짠 코드와 완전히 똑같네요 고생하셨습니다.
    # 여기서 추가 문제를 더 드려볼게요..!
    # 아래 알고리즘으로 검색 메뉴를 실행 해보면, 동명이인을 처리하지 못합니다.
    # (예를 들어, "홍길동"이라는 이름을 갖는 사람 두 명이 추가되어 있다면,
    # "홍길동"이라고 검색 시, 한 명만 출력하는 현상이 발생합니다.)
    # 이 부분에 대해서 한 번 생각해보시고, 여유가 생기실 때 해서 보내주세요!
    # (이 추가과제 또한 의무,필수가 아니니 부담 가지지 마세요!~)
        for data in phoneList:
            print("*" * 20)
            if data["name"] == name:
                print("이름:", data["name"])
                print("전화번호:", data["number"])
                continue
                print("*" * 20)
            else:
                print("ERROR: 찾는 번호가 존재하지 않습니다.")
                return

def delData():
    name = input("이름 입력: ")
    # 여기도 마찬가지로 잘 해주셨습니다!
    # 단, 쬐끔 아쉬운 것이... phoneList.remove() 함수 안에 인자를 전달해줄 때,
    # 그냥 phoneList.remove(data)라고 해주시면 됩니다.
    # 뭐.. 코딩에 정답이 있는 것은 아니라 아주 틀린 것은 아니지만,
    # 최대한 간결하게 코딩하는 버릇을 들이는 것이 중요합니다.
    # 코드의 가독성을 높일 수록 나중에 어떤 버그가 생겨 코드를 수정해야할 때 편해집니다.

    sameNameCnt = 0
    for data in phoneList:
        if data["name"] == name:
            sameNameCnt += 1
            continue

    for data in phoneList:
        if sameNameCnt == 1:
            phoneList.remove(data)
            print(name, "의 연락처를 삭제했습니다.")
            global numOfData
            numOfData -= 1
            return

        elif sameNameCnt > 1:
            number = input("동명이인이 존재합니다. 전화번호를 입력하세요: ")
            if data["number"] == number:
                phoneList.remove(data)
                print(name, "의 연락처를 삭제했습니다.")
                numOfData -= 1
                return
            else:
                break
        else:
            break

    print("ERROR: 찾는 번호가 존재하지 않습니다.")


def showData(): # 전체 출력 (4)
    # 연락처가 존재할 때만
    if numOfData > 0:
        print("*" * 20)
        for data in phoneList:
            print("이름: ", data["name"])
            print("전화번호: ", data["number"])
            print("*" * 20)
    else:
        print("ERROR: 연락처가 없습니다.")


# 시작
while True:

    print("="*20)
    print("Total Contacts: {}".format(numOfData))
    print("1. 전화번호 추가")
    print("2. 전화번호 검색")
    print("3. 전화번호 삭제")
    print("4. 전화번호 전체 출력")
    print("5. 종료 ")
    print("="*20)

    menu = input("메뉴를 선택해주세요: ")

    if menu == "1":
        inputData()

    elif menu == "2":
        searchData()

    elif menu == "3":
        delData()

    elif menu == "4":
        showData()

    elif menu == "5":
        break

    else:
        print("ERROR: 메뉴를 잘못 입력했습니다. 1~5까지 입력해주세요 !")

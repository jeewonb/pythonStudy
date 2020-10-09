
phoneList = []
numOfData = 0

def inputData():

    while True:
        # 입력 받기
        name = input("이름 입력: ")
        number = input("번호 입력: ")
        # 빈칸 아닐 때만
        if name != "" and number != "":
            phoneList.append({"name": name, "number": number})  # 중괄호로 싸여져있으면 Dictionary 자료형
            global numOfData
            numOfData += 1
            return
        else:
            print("*" * 20)
            print("ERROR: 공백없이 입력하세요.")
            continue

def showData():
    # 연락처가 존재할 때만
    if phoneList.__len__() > 0:
        print("*" * 20)
        for data in phoneList:
            print("이름: ", data["name"])
            print("전화번호: ", data["number"])
            print("*" * 20)
    else:
        print("ERROR: 연락처가 없습니다.")

def delData():

    name = input("이름 입력: ")

    for data in phoneList:
        if data["name"] == name:
            phoneList.remove({"name": data["name"], "number": data["number"]})
            global numOfData
            numOfData -= 1
            return
    print("ERROR: 찾는 번호가 존재하지 않습니다.")

def searchData():

    name = input("찾을 이름 입력: ")

    for data in phoneList:
        print("*" * 20)
        if data["name"] == name:
            print("이름:", data["name"])
            print("전화번호:", data["number"])
            print("*" * 20)
            return

    print("ERROR: 찾는 번호가 존재하지 않습니다.")

while True: # 반복문 넣고 indent 꼭 해야 함 !!!

    print("="*20)
    print("Total Contacts: {}".format(numOfData)) # tab 누르면 자동완성
    print("1. 전화번호 추가")
    print("2. 전화번호 검색")
    print("3. 전화번호 삭제")
    print("4. 전화번호 전체 출력")
    print("5. 종료 ")
    print("="*20)

# Add at the last: a.append("World")
# Add: a[3] = ""
# Delete: del a[0] <- 인덱스 번호를 찾아서 삭제
# Delete: a.remove("World") <- 단어를 찾아서 삭제

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


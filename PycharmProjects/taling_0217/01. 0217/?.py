phoneList = []
numOfData = 0

def InputData():
    name = input("이름 입력 : ")
    number = input("번호 입력 : ")
    phoneList.append({"name": name, "number": number})
    global numOfData
    numOfData += 1

def ShowAllData():
    for data in phoneList:
        print("-----------------")
        print("이름 :", data["name"])
        print("번호 :", data["number"])
        print("-----------------")

def SearchData():
    search_name=input("검색할 이름 : ")
    for data in phoneList:
        if data["name"] == search_name:
            print("-----------------")
            print("이름 :", data["name"])
            print("번호 :", data["number"])
            print("-----------------")
            return
    print("찾는 이름이 없습니다.")

def DeleteData():
    search_name = input("삭제할 이름 : ")
    for data in phoneList:
        if data["name"] == search_name:
            phoneList.remove(data)
            global numOfData
            numOfData -= 1
            return
    print("찾는 이름이 없습니다.")


while True:
    print("=====================")
    print("현재 데이터 개수 : {}개".format(numOfData))
    print("1. 전화번호 추가")
    print("2. 전화번호 검색")
    print("3. 전화번호 삭제")
    print("4. 전화번호 전체출력")
    print("5. 종 료")
    print("=====================")
    menu = int(input("선택 >> "))

    if menu == 1:
        InputData()
    elif menu == 2:
        SearchData()
    elif menu == 3:
        DeleteData()
    elif menu == 4:
        ShowAllData()

    elif menu == 5:
        print("종료하겠습니다")
        break
    else:
        print("올바른 선택이 아닙니다.")
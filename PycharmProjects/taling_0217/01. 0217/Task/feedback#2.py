phoneList = []
numOfData = 0


def inputData():
    while True:
        name = input("> 이름을 입력하세요: ")
        number = input("> 번호를 입력하세요: ")
        # 오.. 빈칸 입력 방지 기능까지 넣어주셨네요..! 좋은 아이디어 입니다.
        if name != "" and number != "":
            phoneList.append({"name": name, "number": number})
            global numOfData
            numOfData += 1
            print("=> 연락처가 등록되었습니다.")
            return
        else:
            print("ERROR: 공백없이 입력하세요.")
            continue


def searchData():
    if numOfData < 1:
        print("ERROR: 연락처를 먼저 등록해주세요.")
    else:
        name = input("> 검색할 이름을 입력하세요: ")

        ## searchData() 함수 구현이 잘못되었습니다 ㅠㅠ
        # 예를 들어
        # aaa 라는 이름, bbb 라는 이름, ccc 라는 이름 세명을 저장하고서,
        # ccc를 검색했을 때, 검색 결과가 나오지 않습니다.
        # 아래 코드는 그냥,
        # aaa라는 이름 두명만 딱 저장했을 때, 그 때만 검색결과가 나오게 됩니다.
        # 다시 한번 생각해보시고, 이 버그(?)를 수정해보세요~
        cnt = 0
        for data in phoneList: # 갯수만큼 돈다.
            if data["name"] == name:
                cnt += 1
                print(phoneList.index(data)+1,". 이름:", data["name"], "\t전화번호:", data["number"])
                continue  # 해당 조건을 만족해도 계속 검색

        if cnt == 0:
            print("=> 해당 이름의 연락처가 존재하지 않습니다.")
        print("=> 검색이 종료되었습니다.")


def delData():
    name = input("> 이름을 입력하세요: ")
    sameNameContact = []
    sameNameCnt = 0
    for data in phoneList:
        if data["name"] == name:
            sameNameCnt += 1
            sameNameContact.append({"name": data["name"], "number": data["number"]})

            # continue    # 여기서는 continue 를 없애도 됩니다~

    for data in phoneList:
        if sameNameCnt == 1:
            phoneList.remove(data)
            print("=> ", name, "의 연락처를 삭제했습니다.")
            global numOfData
            numOfData -= 1
            return    # return의 사용법이 적절합니다! 잘하셨네요~


        # 동명이인 삭제 처리를 정말 잘해주셨습니다!~
        # 정말정말 잘해주셨지만, 쪼끄만 팁하나만 말씀드릴게요!
        # 프로그램을 개발할 땐, 이 프로그램을 사용하는 "사용자"를 위한 프로그램을 만들어야 합니다.
        # 아래 코드를 실행했을 때, 동명이인이 존재하면 전화번호를 입력하도록 유도하셨는데,
        # 사용자 입장에서는 사람들의 전화번호를 기억하지 못하고 있을겁니다!(<- 사람들의 전화번호를 기억하고 있다면,
        # 전화번호부 관리 프로그램을 사용할 이유가 없어지게 되죠.)
        # 따라서 아래 설명처럼 프로그램을 개선해보면 어떨까요
        #
        # [개선된 delData() 함수 기능 설명]
        # 동명이인이 있을 경우? => 아래처럼 메시지 출력
        # "동명이인이 존재합니다. 삭제할 번호를 선택해주세요"
        # "1. 010-1234-5678"
        # "2. 010-5678-1920"
        # "3. 010-5312-1428"
        # "입력 >> "
        #
        # 이런 식으로 삭제할 번호를 보여주고, 그 중 선택하라고 했을 때, 사용자의 편의성이 더 개선되겠죠?
        # 개발자는 항상 그 프로그램을 사용할 유저들의 입장에서 생각해보고 개발하려는 습관이 중요한 것 같습니다.
        # 과제해주시느라 고생하셨고,

        elif sameNameCnt > 1:
            print(name,"> 의 동명이인이 존재합니다. 삭제할 번호를 선택해주세요.")
            for i in range(len(sameNameContact)):
                print(i + 1, ". ", sameNameContact[i]["number"])
                continue  # 해당 조건을 만족해도 계속 검색

            delIdx = int(input("> 삭제할 번호 입력: "))
            if delIdx <= sameNameCnt:
                for data in phoneList:
                    if data["number"] == sameNameContact[delIdx-1]["number"] \
                            and data["name"] == sameNameContact[delIdx-1]["name"]:
                        phoneList.remove(data)
                        print("=>", name, "(", data["number"], ")의 연락처를 삭제했습니다.")
                        numOfData -= 1
                        sameNameCnt -= 1
                        return   # return의 사용법이 적절합니다! 잘하셨네요~
                    else:
                        #break  # break 도 굉장히 잘 쓰셨네요
                        continue
            else:
                print("ERROR: 잘못된 번호를 입력하였습니다.")
                return
        else:
            break   # break 도 굉장히 잘 쓰셨네요

    print("ERROR: 찾는 번호가 존재하지 않습니다.")


def showData(): # 전체 출력 (4)
    # 연락처가 존재할 때만
    if numOfData > 0:
        print("=> 검색 결과")
        for data in phoneList:
            print(phoneList.index(data)+1,". 이름:", data["name"], "\t전화번호:", data["number"])
        print("=> 검색이 종료되었습니다.")
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

    menu = input("> 메뉴를 선택해주세요: ")

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
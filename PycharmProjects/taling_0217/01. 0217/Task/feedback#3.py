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


# searchData() 함수 잘 구현해주셨네요! 고생하셨습니다ㅠㅠ 알고리즘도 딱 간결하게 잘해주셨습니다.
def searchData():
    if numOfData < 1:
        print("ERROR: 연락처를 먼저 등록해주세요.")
    else:
        name = input("> 검색할 이름을 입력하세요: ")

        cnt = 0
        for data in phoneList:
            if data["name"] == name:
                cnt += 1
                print(phoneList.index(data) + 1, ". 이름:", data["name"], "\t전화번호:", data["number"])
                continue  # 여기서 이 continue는 없어도 정상적으로 돌아갑니다.
                # 없어도 되고, 있어도 되는 문장은 없애는 것이 좀 더 코드의 가독성이 높아집니다.

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

    # 엇.. 여기 아래에서 첫번째 if 문이 쪼금.. 잘못됐네요 ㅠㅠ
    # 예를 들어, aaa라는 이름 , bbb라는 이름이 추가돼있을 때,
    # bbb라는 사람을 지우겠다고 하면,
    # 엉뚱하게도 aaa라는 사람이 지워지게 됩니다.
    # 따라서 첫번째 if 안의 코드를 살짝 수정해야 하고,
    # 그리고.. 지금 코드가 어떻게든 억지로 돌아가게 만드시기는 했지만..
    # 음.. 제가 더 간결하게 한번 만들어볼게요!
    # 제가 한번 지원님이 짜신 코드 활용해서 간결하게 만들어 볼테니
    # 지원 님이 짜보신 코드와 어떻게 다른지 비교해보시면 좋을 것 같아요!

    if sameNameCnt == 1:
        for i in phoneList:
            if data["name"] == name:
                phoneList.remove(data)
                global numOfData
                numOfData -= 1
                return

    elif sameNameCnt > 1:
        print(name, "> 의 동명이인이 존재합니다. 삭제할 번호를 선택해주세요.")
        for i in range(len(sameNameContact)):
            print(i + 1, ". ", sameNameContact[i]["number"])
        delIdx = int(input("> 삭제할 번호 입력: "))
        if delIdx <= sameNameCnt:
            phoneList.remove({"name": name, "number": sameNameContact[delIdx - 1]["number"]})
            numOfData -= 1
        else:
            print("ERROR: 찾는 번호가 존재하지 않습니다.")

    # for data in phoneList:
    #
    #     if sameNameCnt == 1:
    #         phoneList.remove(data)
    #         print("=> ", name, "의 연락처를 삭제했습니다.")
    #         global numOfData
    #         numOfData -= 1
    #         return
    #
    #     elif sameNameCnt > 1:
    #         print(name,"> 의 동명이인이 존재합니다. 삭제할 번호를 선택해주세요.")
    #         for i in range(len(sameNameContact)):   # range() 함수의 적절한 사용입니다!
    #             print(i + 1, ". ", sameNameContact[i]["number"])
    #             continue  # 여기서도 마찬가지로 continue가 있던 없던 같은 동작을 합니다. continue 지워주셔도 됩니다.
    #
    #         delIdx = int(input("> 삭제할 번호 입력: "))
    #         if delIdx <= sameNameCnt:
    #             for data in phoneList:
    #                 if data["number"] == sameNameContact[delIdx-1]["number"] \
    #                         and data["name"] == sameNameContact[delIdx-1]["name"]:
    #                     phoneList.remove(data)
    #                     print("=>", name, "(", data["number"], ")의 연락처를 삭제했습니다.")
    #                     numOfData -= 1
    #                     sameNameCnt -= 1
    #                     return
    #                 else:
    #                     #break
    #                     continue
    #
    #         # 아래 같은 이런 예외처리는 매우매우 좋습니다!
    #         # 개발할 때 이런 예외처리를 한 두개씩 까먹곤 하는데..
    #         # 잘 캐치하셨네요!
    #         else:
    #             print("ERROR: 잘못된 번호를 입력하였습니다.")
    #             return
    #     else:
    #         break
    #
    # print("ERROR: 찾는 번호가 존재하지 않습니다.")


def showData():  # 전체 출력 (4)
    # 연락처가 존재할 때만
    if numOfData > 0:
        print("=> 검색 결과")
        for data in phoneList:
            print(phoneList.index(data) + 1, ". 이름:", data["name"], "\t전화번호:", data["number"])
        print("=> 검색이 종료되었습니다.")
    else:
        print("ERROR: 연락처가 없습니다.")


# 시작
while True:

    print("=" * 20)
    print("Total Contacts: {}".format(numOfData))
    print("1. 전화번호 추가")
    print("2. 전화번호 검색")
    print("3. 전화번호 삭제")
    print("4. 전화번호 전체 출력")
    print("5. 종료 ")
    print("=" * 20)

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
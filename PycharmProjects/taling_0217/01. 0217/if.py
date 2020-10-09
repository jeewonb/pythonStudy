#print("Hello")


# IF문

# 가격따라 메뉴 맞추기

money = int(input("얼마인가염? : "))

if money >= 10000:
    print("삼겹살")
    money = money - 10000
    print("현재 잔액: {}원".format(money))
    #print("money: " + money.__str__())


elif 5000 <= money < 10000:
    print("제육")
    money = money - 5000
    print("현재 잔액: {}원".format(money))

else :
    print("라면")
    money = money - 2500
    print("현재 잔액: {}원".format(money))

#
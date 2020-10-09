import random
import time

ans = ["일부터 십까지 계산해봅니다", "내가 그린 기린 그림", \
       "안녕 낭연 안녀여영어어어엉"]

result = "fail"

while True:
        #result == "success":

    input("엔터를 누르면 시작합니다.")

    string = random.choice(ans)
    print(">>", string)

    #타자속도: 타이핑 친 문자 개수 / 걸린 시간(초) * 60

    time_start = time.time() # 1972.01.01 부터 시작함

    input_string = input("입력 >> ")

    time_end = time.time()

    if input_string == string:

        speed = len(input_string) * 60 / (time_end - time_start)
        result = "success"

        print("성공 ! 타자 속도: {}타".format(speed))

        break

    else:
        result = "fail"
        print("틀렸습니다. 다시 시작합니다.")

        #continue

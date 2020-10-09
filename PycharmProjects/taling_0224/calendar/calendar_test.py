# import calendar as cal
# as식으로 선언하면 그 다음부터 불러올 때 편함

# 하나만 불러올 때는 아래처럼하면 메모리를 효율적으로 사용할 수 있음

from calendar import prmonth

print(prmonth(2019, 2))

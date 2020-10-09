

import time

date = "{}년 {}월 {}일 {}요일"
a = time.localtime()
print(a)
print(date.format("2019","2","17","일"))


print(date.format(a.tm_year, a.tm_mon, a.tm_mday, "일"))

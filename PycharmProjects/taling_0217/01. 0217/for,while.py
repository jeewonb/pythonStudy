# Question 1
number = 0

for number in range(10):
   number = number + 1

   if number == 5:
      break    # break here

   print('Number is ' + str(number))

print('Out of loop')


# Question 2
number = 0

for number in range(10):
   number = number + 1

   if number == 5:
      continue    # continue here (5에서 끝나지 않고 계속 간다.)
                    # skip this condition and run the loop
   print('Number is ' + str(number))

print('Out of loop')

# Question 3
number = 0

for number in range(10):
   number = number + 1

   if number == 5:
      pass    # pass here

   print('Number is ' + str(number))

print('Out of loop')
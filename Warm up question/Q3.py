number=int(input())
remainder=number%8
if remainder==0:
  print(number)
elif remainder==4:
  print(number-4)
elif remainder>4:
  print(number+8-remainder)
elif remainder<4:
  print(number-remainder)
#Doesn't work for test case 3

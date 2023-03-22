count=0
sum=0
while True:
  number=int(input())
  if number<0:
    break
  elif number>100:
    count+=1
  else:
    sum+=number
print(sum+'\n'+count)

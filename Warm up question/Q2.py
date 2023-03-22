number=str(input())
symbol=input()
if len(number)==2:
  print(symbol*4+'\n'+symbol+number+symbol+'\n'+symbol*4)
elif len(number)==3:
  print(symbol*5+'\n'+symbol+number+symbol+'\n'+symbol*5)
else:
  print(symbol*3+'\n'+symbol+number+symbol+'\n'+symbol*3)

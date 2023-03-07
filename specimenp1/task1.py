#round 1 demo 1
greeting = input()
name = input()
print(greeting + ' ' + name)

#round 2 demo 2 
first=int(input())
second=int(input())
if first>second:
    answer=first - second
    print(answer)
else:
    answer=second-first
    print(answer)
    
#round 3 demo 3
word=input()
length=int(len(word))
words=word
while len(words) <= 30:
    words=words + word
print(words)

#round 4 demo 4
number= int(input())
if number > 50:
    print("yes dream big")
else: 
    print("on the small side")

#round 5 demo 5
number1 = int(input())
sign = input()
number2 = int(input())
if sign=='+':
    print(number1+number2)
else:
    print(number1*number2)

#round 6 demo 6
first=input()
second=input()
third=input()
fourth=input()
fifth=input()
if first=='Ellie':
    print('1st')
elif second=='Ellie':
    print('2nd')
elif third=='Ellie':
    print('3rd')
elif fourth=='Ellie':
    print('4th')
else:
    print('5th')
    
#round 7 demo 7
first=input()
second=input()
if first > second:
    print(second+first)
else:
    print(first+second)
    
#round 8 demo 8
number=int(input())
plant='.|.'+'\n'
print('\./'+'\n'+plant*number)

#round 9 demo 9
thingy=input()
if thingy=='+':
    print('+&><+&><')
elif thingy=='&':
    print('&><+&><+')
elif thingy=='>':
    print('><+&><+&')
else:
    print('<+&><+&>')
    
#round 10 demo 10

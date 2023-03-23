x=int(input())
y=-(int(input()))
n=int(input())
old_deck=[1,2,3,4,5,6,7,8,9]
new_deck=[]
x2=0
y2=-1
n2=0
while n2<=n and old_deck!=[]:
  while x2<=x:
    new_deck.append(old_deck[x2])
    x2+=1
  x2=0
  while y2<=y:
    new_deck.append(old_deck[y2])
    y2-=1
  y2=-1
print(new_deck[1])

word=input()
length=int(len(word))
words=word
while len(words) <= 30:
    words=words + word
print(words)

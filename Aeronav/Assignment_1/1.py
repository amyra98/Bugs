def pattern(data):
 strings = list (data.split())
max = 0

for i in strings:   
    if len(i) > max:
      max = len(i)


width=max + 4

print('*'*width)

for i in range(0, len(strings)):
    print('*', strings[i]+' '*(width - len(strings[i])-4),'*')
print('*'*width)   

 
















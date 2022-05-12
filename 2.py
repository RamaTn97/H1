binary=list()
d=int(input('enter decimal number '))
while d>0:
    binary.append(d%2)
    d//=2
binary.reverse()
for i in binary:
    print(i,end='')



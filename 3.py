infile='t.txt'
infile=open(infile,'r')
n=0
u=input('enter user name: ')
s=""
for i in infile:
    answer=input(i[:i.index(':')])
    if answer == i[i.index(':')+1:].rstrip():
        n+=1
        s+=i+" true/n"
s+=str(n)
print(s)
outfile='new.txt'
outfile=open(outfile,'w')
outfile.writelines(s)
infile.close()
outfile.close()

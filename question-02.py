s=input('enter:')

l=[]
rev=s[::-1]
#print(rev)
d=rev
for i in range (0,len(rev)):
    rev=d 
    for j in range (i+1,len(rev)):
        if rev[j]==rev[i]:
            d=rev.replace(rev[j],'',1) 
s=rev[::-1]         
print('output:',s)    


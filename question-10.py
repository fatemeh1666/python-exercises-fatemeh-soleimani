s=input('enter sentence1:')
t=input('enter sentence2:')
l1=s.split()
l2=t.split()
print('common words:')
#print(l1,len(l1),l2)
for i in range(0,len(l1)):
    for j in range(0,len(l2)):
        if l1[i]==l2[j]:
            print(l1[i])
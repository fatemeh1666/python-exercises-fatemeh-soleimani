s=input('enter sentence: ')
l=s.split()
print(l)
t=["hack", "fraud", "scam" ,"password","attack"]
print(t)
l1=[]
d=0
for i in range(0,5):
    d=0
    for j in range(0,len(l)):
     if t[i]==l[j]:
        d+=1
    l1.append(d)
    
if l1[0]!=0:   
    print('hack-->',l1[0]) 
if l1[1]!=0:    
    print('fraud-->',l1[1])
if l1[2]!=0:
    print('scamm-->',l1[2])
if l1[3]!=0:
    print('password-->',l1[3])
if l1[4]!=0:
    print('attack-->',l1[4])
t=input('enter sentence: ')
l=t.split()
print(l)
b_max=0
b2=0
c_index=0
d=0
for i in range(0,len(l)):
    b2=l.count(l[i])
    if b2>b_max:
        b_max=b2
        c_index=i
        
        
print('output of max iterable is: ',l[c_index] , '-->',b_max)
    
    
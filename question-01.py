l=[15,50,70,1,90,20,4,108,6]
s=l[0]
for i in  range (len(l)) :
    if l[i]>=s:
       s =l[i]
print(s,':maximum')
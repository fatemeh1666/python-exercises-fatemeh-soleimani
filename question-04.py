s=input('رشته را وارد کنید')
c=0
j=0
d=0
for i in s:
    c=c+1
print('طول رشته:',c)
if c%2==0:
    j=c/2
    for i in s:
        if d<j:
           d+=1
           print(i, end='')
d=0
if c%2!=0:
  j=c/2           
  for i in s:     
      if d>j: 
         print(i,end='')
      d+=1
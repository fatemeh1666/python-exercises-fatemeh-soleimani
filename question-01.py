s=input('enter password:')
j=0
k=0
u=0
w=0
if len(s)<8:
    print('password invalid')
    print('password must contain at least 8 character')
for i in s:
    if i.isupper()==True:
        j+=1
    if i.islower()==True:
          k+=1 
    if i.isdigit()==True:
         u+=1
    if i=='@' or i=='#' or i=='$' or i=='%' or i=='^' or i=='&' or i=='*'or i=='!':
        w+=1
if j<1:
    print('password must contain min 1 upper alpha')        
if k<1:
    print('password must contain min 1 lower alpha')
if u<1:
    print('password must contain min 1 digit')  
if w<1:
        print('password must contain  a spacial character')  
if j>=1 and k>=1 and u>=1 and w>=1 and len(s) >=8:
    print('valid')
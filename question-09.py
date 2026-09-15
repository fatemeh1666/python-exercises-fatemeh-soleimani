user='w12345'
pas='12345'
j=0
while (j<4):
    s=input('user is:')
    p=input('password is:')
    if  user==s and pas==p:
        print('login succesfull')
        break
    if user!=s or pas!=p:
        print('wrong username or password')
        print('Attempts remaining:',2-j)
        j+=1
    if j==3:
        break
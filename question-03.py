s=input('enter:')
j=0
k=0
y=0
p=0
w=0
for i in s:
    if i.isupper():
        j+=1
    if i.islower():
            k+=1
    if i.isdigit():
         y+=1
    if i==' ':
          p+=1
    if i=='@' or i=='#' or i=='$' or i=='%' or i=='^' or i=='&' or i=='*' or i=='!':
              w+=1
print(' letters',j+k)              
print('uppercase:',j)
print('lowercase:',k)
print('digit:',y) 
print('space:',p)             
print('special characters:',w)

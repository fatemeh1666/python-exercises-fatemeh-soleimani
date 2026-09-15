s=input('enter:')
u=0
k=0
y=0
p=0
w=0
l=s.split()
#print(l,len(l))
for i in s:
    
    if i.islower():
            k+=1
    if i.isupper():
              u+=1
    if i.isdigit():
         y+=1
    if i==' ':
          p+=1
    if i=='@' or i=='#' or i=='$' or i=='%' or i=='^' or i=='&' or i=='*' or i=='!':
              w+=1
############################طولانی ترین کلمه###################################
#print(l)
b_max=0
c_index=0
l_b_max=[]
l_new_index=[]
for i in range(0,len(l)):
    if len(l[0])<len(l[i]):
      b_max=len(l[i])
      c_index=i
      l_b_max.append(b_max)
      l_new_index.append(i)
#for i in range(0,len(l)):
    if len(l[0])>len(l[i]):
        b_max=len(l[0])
        c_index=0
        l_b_max.append(b_max)
        l_new_index.append(0)
#print('max_charrrr',b_max,'indexxxxx',c_index)
#print(l_b_max)
d_c=0
for j in range (0,len(l_b_max)):
                if l_b_max[j]==b_max:
                   
                    d_c=l_new_index[j]
                    break

#####################################کوتاه ترین کلمه#######################################
b_min=0
c_index1=0
l_b_min=[]
l_new_index1=[]
for i in range(0,len(l)):
    if len(l[0])>len(l[i]):
      b_min=len(l[i])
      c_index1=i
      l_b_min.append(b_min)
      l_new_index1.append(i)
    if len(l[0])<len(l[i]):
          b_min=len(l[0])
          c_index1=0
          l_b_min.append(b_min)
          l_new_index1.append(0)
#print('min_charrrr',b_min,'indexxxxx111111',c_index1)
#print(l_b_min)
dd=0
for j in range (0,len(l_b_min)):
                if l_b_min[j]==b_min:
                    dd=l_new_index1[j]
                    break

############################کلمه ای که بیشترین تکرار را دارد###################
b_mx=0
b2=0
c_ind=0
d=0
for i in range(0,len(l)):
    b2=l.count(l[i])
    if b2>b_mx:
        b_mx=b2
        c_ind=i
        ###########################پرتکرارترین کاراکتر############ 
b_mn=0
b3=0
c_ind2=0
d=0
for i in range(0,len(s)):
    b3=s.count(s[i])
    
    if b3>b_mn:
        b_mn=b3
        c_ind2=i
print('total characters ' ,u+k+y+p )    

print('total word:',len(l))              
print('total letters',u+k)
print('total digit:',y)
print('total space:',p)               
print('total uppercase:',u)
print('total lowercase:',k)
print('longest word:',l[d_c],'.....length:',b_max)  
print('shortest word:',l[dd],'.....length:',b_min)      
print('Most repeted word:',l[c_ind] , '-->',b_mx)         
print('Most repeted characters:' ,s[c_ind2],'-->',b_mn)

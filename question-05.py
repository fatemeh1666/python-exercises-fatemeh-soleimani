t=input('enter sentence:')
#t=('python is the vvvvvvv kkkkkkkk nb kkkkkkkk nn kkkkkkkk')
l=t.split()
#print(l)
b_max=0
b2=0
c_index=0
d=0
l_b_max=[]
l_new_index=[]
for i in range(0,len(l)):
    if len(l[0])<len(l[i]):
      b_max=len(l[i])
      c_index=i
      l_b_max.append(b_max)
      l_new_index.append(i)
    if len(l[0])>len(l[i]):
          b_max=len(l[0])
          c_index=0
          l_b_max.append(b_max)
          l_new_index.append(0)
#print('max_charrrr',b_max,'indexxxxx',c_index)
#print(l_b_max)
ddd=0
for j in range (0,len(l_b_max)):
                if l_b_max[j]==b_max:
                   
                    ddd=l_new_index[j]
                    break
               
print(l[ddd],'length:',b_max)               
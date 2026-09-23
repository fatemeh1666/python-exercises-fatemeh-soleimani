product={'laptop':1200,"phone":800,"tablet":500,"headphone":150,"mouse":50}
l=[]
y=0
y1=0
###################Grantarin mahsool ###########
for i in product.values():
    l.append(i)
y=max(l)#1200
y1=l.index(y)#0
l2=[]
for i in product.keys():
  #   print(i)
     l2.append(i)   
#print(l,l2)
print('Grantarin mahsool:',l2[y1])
###################Arzantarin mahsool#########################
l_vlu=[]
l_key=[]
y2=0
y3=0
for j in product.values():
    l_vlu.append(j)
y3=min(l_vlu)
y4=l_vlu.index(y3)
for k in product.keys():
    l_key.append(k)
print("Arzantarin mahsool:",l_key[y4])
#########################3miyangin###################
t=sum(l)
print("Miyangin ghimatha:",t/len(l))
######################3ghimat>500#########
l5=[]
l6=[]
for m in range (len(l)):
    if l[m]>500:
      #  l5.append(l[m])
        l6.append(l2[m])
      #  print(l[m])
print("mahsoolati ke>500 ghimat darand:",l6)
########################majmoo ghimatha
print("majmoo ghimatha:",t)
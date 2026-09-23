pro={'P01':('Laptop',1200,5),'P02':('Phone',800,0),'P03':('Tablet',500,12),'P04':('Mouse',50,25),
     'P05':('Keyboard',100,0)}
print('mahsoolat mojood:')
####################mahsoolat mojood:
for i in pro:
    if pro[i][2]!=0:
     print(pro[i][0])
print('...............................') 
####################  mahsoolate Namojood  
l=[]    
for j in pro:
 if pro[j][2]==0:
     l.append(pro[j][0])
print('mahsoolate namojood:',l) 
print('...............................')  
###########################stock*price= value(arzesh)  
l1=[]
l2=[]
for k in pro:
    l1.append(pro[k][1]*pro[k][2])
    l2.append(pro[k][0])
    print('stock*price',pro[k][0],'is:',pro[k][1]*pro[k][2])
    
##################### mahsool ba max arzesh    
print('...............................')
y=l1.index(max(l1))
print('mahsool ba max arzesh is:',l2[y],'.... ba arzeshe:',max(l1))
#######################ارزش کل انبار
print('arzeshe kol e anbar is:',sum(l1))

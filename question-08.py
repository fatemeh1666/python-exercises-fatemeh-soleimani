users=[
("Ali",25 ,"python"),
("Sara", 30,"Java"),
("Reza",22, "python"),
("Mina",28, "c++"),
("John", 35,"python"),
("David",30, "Java")
]
d={}
######################گروه بندی براساس زبان
for v1,v2 ,key in users:
    if key in d:
        d[key].append(v1)#اگر کلید موجود بود مقدار جدید را به لیست قبلی اضافه کن
    else:  
        d[key]=[v1]
d_inf={}    
print('Groohbandi:',d)
print('...............................')  
#############################گروه بندی براساس سن  
for v1,v2 ,key in users:
    if key in d_inf:
        
        d_inf[key].append(v2)
        #اگر کلید موجود بود مقدار جدید را به لیست قبلی اضافه کن
    else:  
        d_inf[key]=[v2]
#print(d_inf) 
avg=0
#for i in d_inf:
#t=sum(d_inf[0])
##########################3میانگین سن کاربران هرزبان
for h in d:
 print('avarage age in',h,'...',sum(d_inf[h]))
print('...............................')
 #####################مسن ترین کاربر هرزبان
l=list(d)
w=0
for j in d_inf:
 w=0
 w=max(d_inf[j])
 for i in range(len(users)):
  if users[i][1]==w:
      print('mosentarin karbar  in',j,'...is...',users[i][0],max(d_inf[j]))
 
      ##################3zaban ba max karbar
print('...............................')
m=0 
l=[] 
l_zaban=[]
for h in d:
    l.append(len (d [h]))
    l_zaban.append(h)
mx=0
mx_idx=0    
for i in range(len(l)) :   
    if mx <l[i]:
         mx=l[i]
         mx_idx=i
print('zaban ba bishtarin karbar ...is:',l_zaban[mx_idx])
#######################################3استخراج همه زباهای موجود
print('...............................')
print('hame zabanhaye mojood:')
for h in d:
 print (h)      
      
      
      
      
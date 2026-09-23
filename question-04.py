emp={'E01':{'name':'Ali','age':28,'salary':3000},'E02':{'name':'Sara','age':32,'salary':4500},'E03':{'name':'Reza','age':25,'salary':2800}}
#print(emp)
############max_hooghogh############
w=emp['E01']['salary']
w1=0
for i in emp:
    if w < emp[i]['salary']:
        w=emp[i]['salary']
        w1=i
print('max_hooghogh:',emp[w1]['name'])
############average hoghog#############
avg_hogh=0
j=0
for i in emp:
   avg_hogh+= emp[i]['salary']
   j+=1
print('average hoghogh:',avg_hogh/j)
##################hoghogh>3000##################
for k in emp:
    if emp[k]['salary']>=3000:
        print('in karmand hoghogh>3000 darad  :',emp[k]['name'])
 #############min_hooghogh########################
p=emp['E01']['salary']
p1=0
for i in emp:
     if p > emp[i]['salary']:
         p=emp[i]['salary']
         p1=i
print('minnnn_hooghogh:',emp[p1]['name'])
j=0
sum_l=0
sum_e=0
sum_o=0
for i in range(1,11):
 j=i
 if j%2==0:
    j+=5
    sum_e=sum_e+j  
j=0     
for i in range(1,11):
 j=i
 if j%2!=0:
    j*=5
    sum_o=sum_o+j
    
print('مجموع کل:',sum_e+sum_o)           
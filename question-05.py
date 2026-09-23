stu={'Ali':[18,17,20],'Sara':[15,19,18],'Reza':[12,14,10],'Mina':[20,20,19]}
w=0
sm=[]
k=0
w1=0
avg=[]
mx_avg=0
mx_name=str
#################average
for i in stu:
  w1=0
  for j in range (0,3):
        w1=w1+stu[i][j]
  print(i)
  print('average :',round((w1/3),2)) 
#######################behtarin stu & maximum average 
  if   mx_avg<round((w1/3),2):
        mx_avg=round((w1/3),2)
        mx_name=i
####################status        
  if (w1/3)  >=15:
     print('status:Passed')
  else:
     print('status:Field')
#####################balatarin nomreh     
  print('Max nomreh :',max(stu[i]))
  print('..................')
#sm[k].append(w1)
  #k+=1
print('best student is:',mx_name,'      max average is:',mx_avg)

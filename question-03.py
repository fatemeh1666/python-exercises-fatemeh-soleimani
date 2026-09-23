s=input("enter string:")
d={}
for i in s:
  if i!=' ' or '@' or i=='#' or i=='$' or i=='%' or i=='^' or i=='&' or i=='*' or i=='!':  
    if i in d.keys():
       d[i]+=1
    elif i not in d.keys():
       d[i]=1
       
print(d)

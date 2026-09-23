inventory={"apple":20, "banana":5, "orange":0, "milk":12, "bread":0}
l_val=[]
l_key=[]
l_avai=[]
l_out=[]
s=0
for i in inventory.values():
   # if i>0:
        l_val.append(i)
for j in inventory.keys():
       l_key.append(j)
#print(l_val,l_key)
for k in range(len(l_val)):
    if l_val[k]>0:
       l_avai.append(l_key[k]) 
    if l_val[k]==0:
        l_out.append(l_key[k])
print("Available:",l_avai)
print("AvaOut of stock:",l_out)
print("tedad mahsoolat mojod:",len(l_avai))
print("tedad mahsoolat Na_mojod:",len(l_out))
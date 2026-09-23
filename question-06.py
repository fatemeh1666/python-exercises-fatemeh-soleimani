
sales=(('Ali','Laptop',1200),('Sara','Phone',800),('Ali','Phone',800),('Reza','Laptop',1200)
       ,('Sara','Laptop',1200),('Ali','Mouse',50))

cus={}
for customer , product, price in sales:
    if customer in cus:
        cus[customer]+=price
    else:
        cus[customer]=price
print('kharids har moshtari:',cus)
print('bishtarin kharid:',max(cus,key=cus.get))
pro_count={}
for customer , product, price in sales:
    if product in pro_count:
        pro_count[product]+=1
    else:
        pro_count[product]=1
print('har mahsool chand bar froosh rafteh',pro_count)
total=sum(price for customer,product,price in sales)
print('total sales is',total)
        
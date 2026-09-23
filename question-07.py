orders = [
("Ali", "Laptop"),
("Sara", "Phone"),
("Ali", "Phone"),
("Reza", "Laptop"),
("Sara", "Laptop"),
("Ali", "Tablet"),
("Reza", "Phone")
]
d={}
for key,value in orders:
    if key in d:
        d[key].append(value)#اگر کلید موجود بود مقدار جدید را به لیست قبلی اضافه کن
    else:  
        d[key]=[value]
    
print(d)
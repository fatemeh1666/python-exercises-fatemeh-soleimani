r=0
maxi=0
for i in range (1,11):
 s=int(input('ارتفاع پرش را وارد کنید'))
 if s>maxi:
    maxi=s
    print('بیشترین پرش ثبت شد',maxi)
 elif maxi==s :
     print(' قبلا ثبت شده است')


     
s1=input('رنگ اول را وارد گنید')
s2=input('رنگ دوم را وارد کنید')
s3=input('رنگ سوم را وارد کنید')
if (s1==s2 and s1!=s3 and s2!=s3) or (s1==s3 and s1!=s2 and s3!=s2) or (s2==s3 and s2!=s1 and s3!=s1):
    print('دو رنگ برابرند')
if s1==s2==s3:
        print(' هر سه رنگ برابرند')
if s1!=s2 and s1!=s3 and s2!=s3:
        print(' رنگ ها برابر نیستند')
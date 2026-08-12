account_balance=int(input('موجودی حساب را وارد کنید'))
withdrawal_amount=int(input('مبلغ برداشت را وارد کنید'))
if account_balance>=withdrawal_amount and withdrawal_amount>0:
    print(' عملیات انجام شود')
if account_balance<withdrawal_amount:
    print('عدم موجودی')
if withdrawal_amount<=0:
        print('خطا')
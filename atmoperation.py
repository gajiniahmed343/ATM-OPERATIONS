from atmexcept import DepositError,WithdrawError,InsufficientError
bal=1000.00
def deposit():
    damt=float(input("Enter the  amount that you want to deposit:"))
    if(damt<=0):
        raise DepositError
    else:
        global bal
        bal=bal+damt
        print("Your Account XXXXX123 has credited with amount {}".format(damt))
        print("Your Current Balance INR:{}".format(bal))
def withdraw():
    global bal
    wamt=float(input("Enter the amount that you want to withdraw:"))
    if(wamt<=0):
        raise WithdrawError
    elif((1000+wamt)>bal):
        raise InsufficientError
    else:
        bal=bal-wamt
        print("Your Account XXXXX123 has debited with amount {}".format(wamt))
        print("Your Current Balance INR:{}".format(bal))
def balenq():
    print("Your Current Balance INR:{}".format(bal))
import sys
from atmmenu import atmmenu
from atmexcept import DepositError,WithdrawError,InsufficientError
from atmoperation import deposit,withdraw,balenq
while(True):
    try:
        atmmenu()
        ch=int(input("Enter your choice:"))
        match(ch):
            case 1:
                try:
                    deposit()
                except DepositError:
                    print("Do not enter values lessthan or equal to zero")
                except ValueError:
                    print("Do not enter strs, symbols ")
            case 2:
                try:
                    withdraw()
                except WithdrawError:
                    print("Do not enter values lessthan or equal to zero")
                except InsufficientError:
                    print("Insufficient Funds to Withdraw")
                except ValueError:
                    print("Do not enter strs, symbols ")
            case 3:
                balenq()
            case 4:
                print("Thanks for using the program")
                sys.exit()
            case _:
                print("Invalid Input, Try Again")
    except ValueError:
        print("Do not enter strs, symbols ")
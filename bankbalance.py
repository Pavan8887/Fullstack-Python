'''bankbalance = 5000
pin = 1234

withdraw_ammount =int(input("enter your ammount"))
user_password =int(input("enter your pin"))

if withdraw_ammount <=bankbalance and user_password == pin:
    bank_balance = bankbalance - withdraw_ammount
    print("withdraw allowed")
    print("remaining balance is ",bank_balance)
else:
    print("withdraw not allowed")'''

def withdraw_money():
    pin =int(input("Enter your pin"))
    if pin == 1234:
        print("pin is correct")
        ammount =int(input("enter a ammount"))
        bank_balance =int(input("Enter your ammount"))
        if ammount <= bank_balance:
            print("Withdrawal is successfull")
            rem_balance = bank_balance - ammount
            print("Remaining balance is ",rem_balance)
        else:
            print("Insuffiecient balance")
    else:
        print("Incorrect pin")
withdraw_money()



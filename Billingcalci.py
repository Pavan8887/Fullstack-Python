
'''units = int(input("Enter units "))
if units <= 100:
    basic_price = units * 2

elif units <=200:
    basic_price =units*3

else:
    basicprice = units * 5

discount = basic_price * 0.1

additional_charges = 50

print("total bill :",basic_price - discount + additional_charges)'''


'''product = int (input ("Eneter a number"))
price = int(input("Enter a price "))
quantity = int(input("Enter a quantity"))
discount = int(input("Enter a discount "))

total = (price * quantity)
final_price = total - discount
print("Total price is ",final_price)'''

'''password = int(input("enter a password"))

if password == 1234:
    print("password is correct")
else :
    print("password is incorrect")'''

'''age = int(input("enter your age "))
if age >=18:
    print("eligible for voting")

else:
    print("not eligible for voting")'''

'''student = int(input("ENTER YOUR MARKS"))
if student >=90:
    print("JOB")
elif student >=50:
    print("college")
elif student >=35:
    print("BBMP")

else:
    print("TEA SHOP")'''


'''age = int(input("Enter your age "))
salary =int(input("Enter your salary"))'''

'''if age >=18 and salary>=500000:
    print("Approved for loan")
else:
    print("Not approved for loan")'''

'''if age >=18 or salary>=50000:
    print("Approved for loan")
else:
    print("Not approved for loan")'''


'''bank_balance = 5000
password = "1234"

withdraw_ammount =int(input("enter your ammount"))
user_password =int(input("enter your password"))

if withdraw_ammount <=bank_balance and user_password == password:
    bank_balance = bank_balance - withdraw_ammount
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




          





 
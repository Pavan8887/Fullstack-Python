'''encapsulation means wrapping variables and methods togather inside a class and comtrollimg acess of data'''

'''WITHOUT ENCAPSULATION'''

# class bank:
#     def __init__(self):
#         self.balance = 10000

# acc = bank()
# acc.balance = 1000000
# print(acc.balance)

'''WITH ENCAPSULATION'''

# class bank:
#     def __init__(self):
#         self.__balance = 10000
#     def deposit(self, ammount):
#         self.__balance += ammount
#     def show_balance(self):
#         print(self.__balance)
# acc=bank()
# acc.deposit(500)
# acc.show_balance()

'''GETTER'''

# class employee:
#     def __init__(self,salary):
#         self.__salary = salary
#     def get__salary(self):
#         return self.__salary
    
# emp = employee(5000)
# print(emp.get__salary())

'''SETTER'''

# class employee :
#     def __init__(self):
#         self.__salary = 100

#     def set_salary(self,ammount):
#         if ammount > 0 :
#             self.__salary = ammount
#         else:
#             print("Invalid salary")

#     def get_salary(self):
#         return self.__salary
    
# emp = employee()
# emp.set_salary(632363)
# print(emp.get_salary())


'''POLYMORPHISM '''

'''Polymorpism means the same method name can perform different action dpending on the project'''

# class dog:
#     def sound(self):
#         print("dog barks")

# class cat:
#     def sound(self):
#         print("cat meows")

# Dog = dog()
# Cat = cat()

# Dog.sound()
# Cat.sound()

# class bank:
#     def sucess(self):
#         print("Payment is sucessfull")
# class Upi:
#     def sucess(self):
#         print("Payment unsucessfull")

# upi = bank()
# cash = Upi()

# upi.sucess()
# cash.sucess()


'''ABSTRACTION'''


'''Absraction means hidign internal implementation and  showing only necessary feature to the user'''


# from abc import ABC ,abstractmethod
# class vechile(ABC):
#     @abstractmethod
#     def start(self):
#         pass

# class car(vechile):
#     def start(self):
#         print("Car started")

# car = car()
# car.start()

from abc import ABC,abstractmethod

class vechile(ABC):
    @abstractmethod
    def start(self):
        pass 

class Dog():
    def bekku(self):
        print("Dog barkes")

class cat(Dog):
    def bekku(self):
        print("cat meows")

class monkey(Dog):
    def bekku(self):
        print("monkey eats banana")

class cow(Dog):
    def bekku(self):
        print("cow eats grass")

Dog = Dog()
cat = cat()
monkey = monkey()
cow = cow()
Dog.bekku()
cat.bekku()
monkey.bekku()
cow.bekku()


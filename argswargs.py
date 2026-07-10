#KWARGS
'''def add(*numbers):
    print(numbers)
add(10,20,30,40,50,60)


def add(*num):
    total = 0
    for i in num:
        total += i
    print(total)
add(10,20,30)'''



#KWARGS

'''def student(**values):
    print("name:",values["name"])
    print("age :",values["age"])
    print("branch:",values["branch"])
student(
    name = "pavam",
    age =21,
    branch ="hah",'''


#SQUARE ROOT
'''def sqrt(a):    
   result =  a**0.5
   print(result)
sqrt(4)'''

#SQUARE
'''def square(a):
    result = a * a
    print(result)
square(4)'''

#BY USING LAMBDA FUNCTION

'''sqaure = lambda x:x*x
print(square(4))


add = lambda a,b:a+b
print(add(1,2))'''

evenodd = lambda x : "Even" if x%2==0 else "Odd"
print(evenodd(6))
print(evenodd(7))
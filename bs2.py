#odd or even
a=int(input("enter a number: "))
if(a % 2== 0):
    print("even")
else:
    print("odd")

#greatest of 3 numbers
a1=int(input("enter a number: "))
a2=int(input("enter a second number: "))
a3=int(input("enter a third number: "))

if(a1>a2 and a1>a3):
    print("a1 is larger",a1)
elif(a2>=a3):
    print("a2 is larger",a2)
else:
    print("a3 is larger",a3)

#multiple of numbers
b=int(input("enter a number: "))

if(b % 7== 0):
    print("True")
else:
    print("False")
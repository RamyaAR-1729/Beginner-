#to check a prime number
num=int(input("enter a number: "))
if num==0 or num==1:
    print(num, "is not a prime number")
elif num>1:
 for i in range(2,num):
    if(num%i)==0:
        print(num,"is not a prime number")
        print(i,"times",num/i,"is",num)
        break
 else:
    print(num,"is a prime number")
else:
    print(num,"is not a prime number")

#area of a triangle
a=5
b=6
c=7
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print('the area of the triangle is %0.2f' %area)

#set in pyton
#s={"Geeks","for","Geeks"}
#print(s)
#s[1]="Hello"     #this will show error because set cannot have duplicates and immutable 
#print(s)

#frozen set
s=set(["a","b","c"])
print("normal set")
print(s)

fs=frozenset(["e","f","g"])
print("\nfrozen set")
print(fs)

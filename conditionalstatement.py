#if condition
a=20

if(a >= 18):
    print("eligible to vote")

#if-else condition
a=int(input("enter the age: "))

if(a>=18):
    print("eligible for vote and having a driving licence")
else:
    print("not eligible")

#if-elif-else condition
a=int(input("enter the marks: "))

if(a>=90):
    grade="A"
elif(a>=80 and a<90):
    grade="B"
elif(a>=70 and a<80):
    grade="C"
else:
    grade="D"

print(grade)
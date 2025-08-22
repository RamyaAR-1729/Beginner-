student=["karan", 95.4, 17, "delhi"]
print(student)
print(type(student))

#indexing
print(student[0])

#mutable
student[0]="arjun"
print(student)

#list slicing
marks=[85, 94, 76, 63, 48]
print(marks[1:4])
print(marks[:-1])

#list methods
list=[2, 1, 3]
list.append(4)
print(list)

list.sort()
print(list)

list.sort(reverse=True)
print(list)

list.reverse()
print(list)

list1 =[2,1,3]
list1.insert(1,5)
print(list1)

a=[1, 2, 1, 3]
a.remove(1)
print(a)
a.pop(0)
print(a)
str1 = "this is a string."
str2 = 'ramya'
str3 = '''this is a string'''

print(str1)

#string operations
#concatination
print(str1+" "+str2)

#length
str="hello"
len1=len(str)
print(len1)

#indexing
a="hello world"
ch=str[2]
print(ch)

#slicing
print(str[1:5])

#negetive indexing
print(str[-5:-2])

#string functions
str="i am a coder."
c=str.endswith("er.")
print(c)

d=str.capitalize()
print(d)

e=str.replace("a","an")
print(e)

f=str.find("a")
print(f)

g=str.count("a")
print(g)
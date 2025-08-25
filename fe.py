#writing  a python program to demonstrate packing and unpacking and appending data to tuple
my_tuple=(1,'hello',3.14,'world')
print(f"original tuple:{my_tuple}") 
print(f"first element:{my_tuple[0]}")
print(f"last element:{my_tuple[-1]}")
a,b,c,d=my_tuple
print(f"unpacked values:a={a},b={b},c={c},d={d}")
nested_tuple=(1,[2,3],'four')
nested_tuple[1].append(4)
print(f"tuple with modified nested list:{nested_tuple}")

#operations on tuple
samptuple1=(1,2,3,'apple','banana')
print(samptuple1)
print(f"original tuple:(samptuple1)")
print(f"first element:(samptuple[0])")
print(f"last element:(samptuple[-1])")
print(f"sliced tuple (element from index 1to 3):(samptuple1[1:4])")
a,b,c,d,e=samptuple1
print(f"unpacked variables:a={a},b={b},c={c},d={d},e={e}")
print(f"'apple' in samptuple1:{'apple' in samptuple1}")
print(f"length of tuple:{len(samptuple1)}")

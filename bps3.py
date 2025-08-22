#adding 3 movies to list 
movie=[]
m1=movie.append(input("enter the 1st movie: "))
m2=movie.append(input("enter the 2nd movie: "))
m3=movie.append(input("enter the 3rd movie: "))
print(movie)

#checking if it is palindrome
list=[1,2,1]
copy_list=list.copy()
copy_list.reverse()
if(copy_list == list):
    print("palindrome")
else:
    print("not a palindrome")

#counting the tuple
tup=("A", "C", "D", "A", "B", "A")
print(tup.count("A"))

#sorting
print(tup.sort())

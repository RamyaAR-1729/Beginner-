info={
    "name":"ramya",
    "a":["ramya","sita","c"],
    "topics":("dict","set"),
    "age":35,
    "is_adult":True
}
print(info)
print(type(info))

#index
print(info["name"])

info["name"]="ramyaraj"
print(info)

null_dict={}
print(null_dict)
null_dict["name"]="raju"
print(null_dict)

#nested dictionaries
student={
    "name":"kartik gowda",
    "subject":{
        "phy":97,
        "chem":98,
        "math":95
    }
}
print(student)
print(student["subject"])
print(student["subject"]["chem"])

#methods
print(student.keys())
print(len(list(student.keys())))

print(student.values())
print(len(student.values()))

pairs=list(student.items())
print(pairs[0])

print(student["name"]) #if the value wrong it will return error
print(student.get("name")) #this will return none

student.update({"city":"delhi"})
print(student)
new_dict={"city":"delhi"}
student.update(new_dict)
print(student)
my_dict = {
    "name" : "Archit",
    "age" : 12,
    "weight" : 35.5,
    "student" : True,
}

print(my_dict)

#accessing a value of a key
print(my_dict["name"])

#edit the value of a key
my_dict["age"] = 13
print(my_dict)

#add item in the dictionary
my_dict["Gender"] = "Male"
print(my_dict)

#Eliminate the key value from the dictionary
my_dict.pop("weight")
print(my_dict)

#get the value of a key using get method
name = my_dict.get("name")
print(name)

#clear the dictionary
my_dict.clear()
print(my_dict)
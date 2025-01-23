print("hello wolrd")
print(42) #integer
print(3.14) #float
print(True) #boolean
print(None) #NoneType
print([])
print(())
print({})


ages = [23, 45, 56, 78] #list
print(ages)
print(f"the type of {ages} is {type(ages)}")
user = {"Name": "Calvin", "age": 18, "Address": "Florida, Mzanzi", "Gender": "Male"} #dictionary 
print(user)

#reading datatypes
print (f"the ages of the first person is: {ages[0]} years old")
print (f"the second person is: {ages[1]} years old")

print(user["Name"]) #slicingg
print("range(10)") #range


greet = 'Hello World!'
name = "calvin"
introduce = greet+f'\nMy name is {user["Name"]} and I am {user["Gender"]}' #string concatenation
print(introduce)
print({"Calvin", 23})
#user =(user["name"], user["age"]) #Tuple
print(user)
#print(user[1]) #indexing
print(user)

#boolean

"""Author: joel
   date: 2025-01-11
   decription: This is a multiline comment
   License: MIT
   """
is_adult = False

if user["age"] >= 18:
    is_adult = True  #constant name "is_adult" doesn't conform to upper_case namin style
    print("you are an adult")
else:
    print("you are a minor")

print(is_adult)

"""check if the user is a minor or an adult"""  #string statment has no effect
if user["age"] < 18:
    print("you are a minor")
else:
    is_adult = True
    print("you are an adult")

if is_adult:
    print("you are allowed to drink alcohol")
else:
    print("you arre not allowed to drik alcohol")


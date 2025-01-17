introduce = "Hello World"

introduce = introduce.upper() #string methods
print(introduce)

def say_hi(first_name, last_name):
    name =first_name + '' + last_name
    return f"Hello {name}!"


print(say_hi("Calvin", "Safoukou" .capitalize())) #Fontion call
print(say_hi("Toure".upper(), "Bonaberi".lower()))


def add(a,b):
    return a + b

x = 12.5
y = 14.8
print(f"The sum of {x} and {y} is {add(x,y)}")

def divide(a,b):
    if b>0:
        if a==0:
            return "Zero divide by any number is zero"
        return a/b
    else:
        return "Division by Zero is not allowed"

def divide2(a,b):
    result = a/b if b>0 else "divisionby zero is not allowed"
    return result

def is_float(num, name):
    if (type(num)==float) or name== 'joel':
        return True
    return False





def divide2(a,b):
    result = a/b if b>0 else "division by zero is not allowed"
    return result
    
def is_float(num, name):
    if (type(num)==float) or name=="joel":
        return True
        return False
    
print(abs(round(divide2(-4,58), 3)))

print(is_float(divide2(9,2), "herve"))


student_name =["Calvin", "Jules", "joel"]
student_ages =[23, 45, 56, 76, 89] 

for index, first_name in enumerate(student_name):
    age =student_ages[index]
    print(f"{first_name} is {age} years old")
    
    
cities =[{"Douala": "Littoral", "yaoude": "Centre"}, {"Johannesburg": "Gauteng"}, 
        {"Nairobi": "Kenya"}]
cities2 = {"Douala": "Littoral", "Yaounde": "Centre", "Bafoussam": "West", "Bamenda": "North West", "Buea": "South West", 
               "Garoua": "North", "Maroua": "Far North", "ngaoundere": "Adamawa",
               "Ebolowa": "South", "Kribi": "South", "Limbe": "South West"}
print(cities[0]["Douala"])
print(cities2["Douala"])

for key in cities:
    print(key)

for city in cities2.values():
    print(city)


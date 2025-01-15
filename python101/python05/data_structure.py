#for loop

#list
employees_names =["caalvin", "joel", "Nathalie","Goby", "herve"]
for name in employees_names:
    #if condition
    if(name == "Calvin"):
        print(f"Hello {name}, get well soon!")
    elif(name=="Calvin"):
        print(f"Hello {name}, you are rocking!")
    elif(name=="joel"):
        print(F"hELLO {name}, you are doing great")
    else: 
        print("Hello", name)


#dictionary and list
employees ={"Jules":[3000, "Data scientist", "german"], 
           "joel":[5000, "machine learning ingenieer", "german"],
           "calvin":[30000, "data engineer", "usa"]}
print(employees["Jules"])

for name, employees_info in employees.items():
    print(f"Name: {name}")
    print(f"salary: {employees_info[0]}")
    print(f"Role: {employees_info[1]}")
    print(f"country: {employees_info[-1]}")


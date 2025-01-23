def difference_two_number(a,b):

    return a-b

remov_a_b = difference_two_number(100, 56)
print(remov_a_b)


def division_two_num(c,d):
    
    return c // d

print(division_two_num(50, 2.3))

print(difference_two_number(90, 5))


def full_name(first_name, last_name):

    return f"My full name is: {first_name} {last_name}"

print(full_name("calvin", "safoukou"))



def add_list_num(grades):
    result = 0
    for i in range(len(grades)):
        print(grades[i])
        result += grades[i]
    return result

print(add_list_num([23, 45, 67, 78]))



def add_list_num2(grades):
    result = 0
    for grade in grades:
        result = result + grade
    return result


print(add_list_num2([23, 45, 67, 78]))


#sort elements
def sort_elements(num):
    return sorted(num)

print(sort_elements([34, 98, 56, 99, 24]))

def add_small_elelemts(num):
    sorted_num = sorted(num)
    print(sorted_num)

    return sorted_num[0] + sorted_num[1]
print(add_small_elelemts([34, 98, 56, 99, 24]))





def is_uppercase(inp):
    sorted_inp = sorted(inp)
    return sorted(inp)[0] + sorted(inp)[1]



def number(lines): 
    return [f"{n + 1}: {line}" for n, line in enumerate(lines)]
    

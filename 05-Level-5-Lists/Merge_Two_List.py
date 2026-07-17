def merge(a,b):
    return a+b
    
print("Merge Two List : ",merge([1,2,3],[4,5,6]))


print("*" * 40)


def merge(a,b):
    result= []

    for num in a:
        result.append(num)

    for num in b:
        result.append(num)

    return result
    
print("Merge Two List : ",merge([1,2,3],[4,5,6]))

def common(a,b):
    num1=set(a)
    num2=set(b)
    
    return num1 & num2


print(common([1,2,3,4,5],[6,2,5,3,7]))


print("*" * 40)

def common(a,b):
    result=[]

    for num in a:
        if num in b and num not in result:
            result.append(num)
    return result

print(common([1,2,3,4,5],[6,2,5,3,7]))






def second(s):
    n=len(s)

    for i in range(n):
        for j in range(n-i-1):
            if s[j]>s[j+1]:
                s[j],s[j+1] = s[j+1],s[j]
                
    return s[-2]

print("Second Largest Number",second([1,23,43,2,53]))



print("*" * 40)


def second(s):
    s = sorted(s)
    
    return s[-2]
print("Second Largest Number",second([1,23,43,2,53]))


print("*" * 40)



def second(s):
    n=len(s)
    second_largest=float('-inf')
    largest=float('-inf')

    for num in s:
        if num> largest:
            second_largest= largest
            largest = num

        elif num > second_largest and num != largest:
            second_largest = num
    return second_largest

print("Second Largest Number",second([1,23,43,2,53]))

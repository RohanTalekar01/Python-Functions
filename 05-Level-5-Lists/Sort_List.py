def sort(s):
    n=len(s)
    
    for i in range(n):
        for j in range(n-i-1):
           if  s[j]> s[j+1]:
               s[j],s[j+1]=  s[j+1],s[j]
    return s

    
print(sort([5,2,3,4,1]))

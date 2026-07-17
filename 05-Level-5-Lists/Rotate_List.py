def rotate(num,k):
    k = k % len(num)
    return num[k:] + num[:k]
    
print(rotate([1,2,3,4,5],2))

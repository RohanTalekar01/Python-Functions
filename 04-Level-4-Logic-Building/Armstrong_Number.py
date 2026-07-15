def armstrong(num):
    digits = str(num)
    n=len(digits)
    return num== sum(int(d) **n for d in digits)

num= 9474

if armstrong(num):
   print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")

    

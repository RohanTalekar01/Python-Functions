def prime_number(number):
    if number<=1:
        return False

    for i in range(2,int(number ** 0.5) + 1):
        if number % i ==0:
            return False
        return True

num=int(input("Enter A Number : "))

if prime_number(num):
    print(f"{num} is a Prime Number ")
else:
    print(f"{num} is Not a Prime Number")

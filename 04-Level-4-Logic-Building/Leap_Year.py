def year(number):
    if (number%4==0 and number % 100 !=0) or (number % 400 == 0):
        return True
    return False

num=int(input("Enter a Year : "))
if year(num):
    print(f"{num} is a Leap Year")
else:
    print(f"{num} is Not a Leap Year")


for y in [1900, 2000, 2023, 2024]:
    print(y, year(y))

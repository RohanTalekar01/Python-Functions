def count(v):
    c = sum(1 for ch in v if ch in "aeiouAEIOU")
    print("Count Vowels : ", c) if c > 0 else print("Vowels Not Present")

count("I AM ROHAN")

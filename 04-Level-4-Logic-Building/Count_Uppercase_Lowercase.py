def count_case(s):
    upper = sum(1 for ch in s if ch.isupper())
    lower = sum(1 for ch in s if ch.islower())
    return upper, lower

text = "I AM Rohan"
u, l = count_case(text)
print(f"Uppercase: {u}, Lowercase: {l}")

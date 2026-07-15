def count_consonants (s):
    vowels="aeiouAEIOU"
    c=0
    for ch in s:
        if ch.isalpha() and ch not in vowels:
            c += 1
    return c

text="I AM ROHAN"
print("Consonants:", count_consonants (text))

def is_palindrome(s):
    s=str(s).lower().replace(" ", "")
    return s== s[::-1]
    
text="Madam"

if is_palindrome(text):
    print(f"{text} is Palindrome")
else:
    print(f"{text} is Not Palindrome")

def count_words(s):
    words = s.split()
    return len(words)

sentence = "I AM ROHAN and I love Python"
print("Word count:", count_words(sentence))

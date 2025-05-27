def count_vowels(s):
    vowels="aeiou"
    count=0
    a=s.lower()
    for char in a:
        if char in vowels:
            count+=1
    return count

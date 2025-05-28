def count_consonants(s):

    # Your code here
    count=0
    vowels="aeiou"
    a=s.lower()
    for char in a:
        if char.isalpha() and char not in vowels:
            count+=1
    return count
            

def remove_duplicates(s):
    a=""
    for char in s:
        if char not in a:
            a+= char
    return a

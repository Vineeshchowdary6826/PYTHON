def reverse_list(lst):
    l=[]
    i=len(lst)-1
    for j in range(len(lst)):
        
        if i>=0:
            l.append(lst[i])
            i-=1
    return l
    

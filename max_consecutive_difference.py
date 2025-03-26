def max_consecutive_difference(lst):
    maxdiff=0
    for i in range(len(lst)-1):
        diff = lst[i] - lst[i+1]
        maxdiff = max(maxdiff,abs(diff))
    return maxdiff
        

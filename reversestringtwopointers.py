def reverse_list(lst):
    start=0
    end=len(list)-1
    
    while start < end:
        lst[start],lst[end]=lst[end],lst[start]
        start+=1
        end-=1
    return lst
    

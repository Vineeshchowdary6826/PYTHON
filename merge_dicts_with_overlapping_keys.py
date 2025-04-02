def merge_dicts_with_overlapping_keys(dicts):
    mergeddict={}
    for i in dicts:
        for key,value in i.items():
            mergeddict[key] = mergeddict.get(key, 0) + value
            
    return dict(mergeddict)
    

def uniqueValues(aDict):
    '''
    aDict: a dictionary
    returns: a sorted list of keys that map to unique aDict values, empty list if none
    '''
    # Your code here
    unique = []
    not_unique = []
    unique_keys = []
    for key in aDict:
        if aDict[key] in unique:
            not_unique.append(aDict[key])
        else:
            unique.append(aDict[key])
            unique_keys.append(key)
        print(f'{key} :')
        print('unique: ', unique)
        print('not_unique', not_unique)
        print('unique_key', unique_keys)
    unique_keys_copy = unique_keys.copy()
    for values in unique_keys_copy:
        if aDict[values] in not_unique:
            unique_keys.remove(values)
    unique_keys.sort()
    return unique_keys


            
print(uniqueValues({1:1, 0:1, 2:4, 4:4, 5:4, 6:5, 7:5}))
import numpy as np

def find_combination(choices, total):
    """
    choices: a non-empty list of ints
    total: a positive int
 
    Returns result, a numpy.array of length len(choices) 
    such that
        * each element of result is 0 or 1
        * sum(result*choices) == total
        * sum(result) is as small as possible
    In case of ties, returns any result that works.
    If there is no result that gives the exact total, 
    pick the one that gives sum(result*choices) closest 
    to total without going over.
    """
    pathQueue = [[1], [0]]
    for x in range(2, len(choices) + 1):
        while len(pathQueue[0]) != x:
            temp = pathQueue.pop(0)
            pathQueue.append(temp + [1])
            pathQueue.append(temp + [0])
    
    choices = np.array(choices)
    lst_diff = []
    combinations = [np.array(x) for x in pathQueue]
    for x in combinations:
        lst_diff.append(abs(np.sum(np.multiply(choices, x)) - total))
    sort_diff = sorted(range(len(combinations)), key = lambda x: (lst_diff[x]) + sum(combinations[x]))
    for x in sort_diff:
        if sum(combinations[x] * choices) <= total:
            return combinations[x]

    

        
    

print(find_combination([3, 10, 2, 1, 5], 12))






    

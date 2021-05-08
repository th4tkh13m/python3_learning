#paste your code here
def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing. 
    In case of a tie for the longest run, choose the longest run 
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run. 
    """
    best_increasing = []
    best_increase_start = 0
    temp_increasing = []
    temp_increase_start = 0

    temp_decreasing = []
    temp_decrease_start = 0
    best_decreasing = []
    best_decrease_start = 0

    trend = None
    for i in range(len(L)):
        if i == 0:
            continue
        if L[i] > L[i-1]:
            if trend not in ['increasing', 'equal']:
                temp_increasing = []
                temp_increasing.append(L[i - 1])
                temp_increase_start = i - 1
                
                if len(temp_decreasing) > len(best_decreasing):
                    best_decreasing = temp_decreasing.copy()
                    best_decrease_start = temp_decrease_start
            trend = 'increasing'        
            temp_increasing.append(L[i]) 
            print(f'current i: {i}, current val : {L[i]}') 
            print('temp_increasing:',temp_increasing)
        elif L[i] < L[i-1]:
            if trend not in ['decreasing', 'equal']:
                temp_decreasing = []
                temp_decreasing.append(L[i - 1])
                temp_decrease_start = i - 1

                if len(temp_increasing) > len(best_increasing):
                    best_increasing = temp_increasing.copy()
                    best_increase_start = temp_increase_start
            trend = 'decreasing'
            temp_decreasing.append(L[i])
            print(f'current i: {i}, current val : {L[i]}')
            print('temp_decreasing:',temp_decreasing)
        else:         
            if i == 1:
                temp_decreasing.append(L[i-1])
                temp_increasing.append(L[i-1])
            if trend != 'decreasing':
                temp_increasing.append(L[i])   
            elif trend != 'increasing':
                temp_decreasing.append(L[i]) 
            trend = 'equal'
            print(f'(equal) current i: {i}, current val : {L[i]}')
            print(temp_decreasing, temp_increasing)

        if i == len(L) - 1:
            if trend == 'increasing':
                if len(temp_increasing) > len(best_increasing):
                    best_increasing = temp_increasing.copy()
                    best_increase_start = temp_increase_start
            elif trend == 'decreasing':
                if len(temp_decreasing) > len(best_decreasing):
                    best_decreasing = temp_decreasing.copy()
                    best_decrease_start = temp_decrease_start
            else:
                if len(temp_decreasing) > len(best_decreasing):
                    best_decreasing = temp_decreasing.copy()
                    best_decrease_start = temp_decrease_start
                if len(temp_increasing) > len(best_increasing):
                    best_increasing = temp_increasing.copy()
                    best_increase_start = temp_increase_start
    print(best_decrease_start, best_decreasing, best_increase_start, best_increasing)
    if len(best_decreasing) > len(best_increasing):
        return sum(best_decreasing)                          
    elif len(best_decreasing) < len(best_increasing):
        return sum(best_increasing)
    else:
        if best_decrease_start < best_increase_start:
            return sum(best_decreasing)
        else: 
            return sum(best_increasing)
print(longest_run([2,1,1,2]))
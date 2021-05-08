def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    if L == []:
        return float('NaN')
    else:
        sum_length = 0
        variance = 0
        for word in L:
            sum_length = sum_length + len(word)
        mean = sum_length/len(L)
        for word in L:
            variance = variance + ((len(word) - mean)**2/len(L))
        return variance**(1/2)
print(stdDevOfLengths(['apples', 'oranges', 'kiwis', 'pineapples']))


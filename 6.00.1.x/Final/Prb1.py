def sum_digits(s):
    """ assumes s a string
        Returns an int that is the sum of all of the digits in s.
          If there are no digits in s it raises a ValueError exception. """
    ans = 0
    count_digit = 0
    for element in s:
        try:
            num = int(element)
            count_digit += 1
            ans += num
        except ValueError:
            continue
    if count_digit == 0:
        raise ValueError
    return ans
print(sum_digits('1ab'))
def sumDigits(s):
    '''Assumes s is a string
    return the sum of the decimal digits in s'''
    try:
        lens=len(s)
        print(lens)
    except TypeError:
        print('You should input a string.')

sumDigits('abcd1')

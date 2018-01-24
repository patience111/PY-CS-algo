def factI(n):
    '''Assumes n an int>0
    returns n!'''
    result=1
    while n>1:
        result=result*n
        n-=1
    return result
def factR(n):
    '''Assumes n an int>0
    Returns n!'''
    if n==1:
        return n
    else:
        return n*factR(n-1)

print(factI(7))
print(factR(7))

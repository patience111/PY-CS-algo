def isPalindrom(s):
    '''Assume s is a str Return True
    if letters in s form a palidrom; F
alse otherwise. Non-letters and capita    lization are ignored.'''
    def toChars(s):
        s=s.lower()
        letters=''
        for c in s:
            if c in 'abcdefghighklmnopqrstuvwxyz':
                letters=letters+c
        return letters
    def isPal(s):
        print(' isPal call with',s)
        if len(s)<=1:
            print(' About to return True from base case')
            return True
        else:
            answer=s[0]==s[-1] and isPal(s[1:-1])
            print(' About to return', answer,'for',s)
            return answer
    return isPal(toChars(s))
def testIsPalindrome():
    print('Try dogGod')
    print(isPalindrom('dogGod'))
    print('Try doGood')
    print(isPalindrom('doGood'))
testIsPalindrome()

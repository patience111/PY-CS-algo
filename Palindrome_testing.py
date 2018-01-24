def isPalindrom(s):
    '''Assume s is a str Return True 
    if letters in s form a palidrom; False otherwise. Non-letters and capitalization are ignored.'''
    def toChars(s):
        s=s.lower(s)
        letters=' '
        for c in 'abcdefjhijklmnopqrstuvwxyz':
            letters=letters+c
        return letters
    def isPal(s):
        if len(s)<=1:
            return True
        else:
            return s[0]==s[-1] and isPal(s[1:-1])
    return isPal(toChars(s))


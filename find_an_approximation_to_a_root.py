def findroot(x,power,epsilon):
    '''Assume x and epsilon int or float, power an int, epsilon>0 & power>=1
    returns float y such that y**power is within epsilon of x. If such a float does not exist, it returns None.'''
    if x<0 and power%2==0:
        return None #Nagtive number has no even-powered roots
    low=min(-1,x)
    high=max(1,x)
    ans=(high+low)/2
    while abs(ans**power-x)>=epsilon:
        if ans**power<x:
            low=ans
        else:
            high=ans
        ans=(high+low)/2.0

    return ans
def testfindroot():
    epsilon=0.0001
    for x in [0.25,-0.25,2,-2,8,-8]:
        for power in range(1,4):
            print('Testing x=',str(x),'and power=',power)
            result=findroot(x,power,epsilon)
            if result==None:
                print('  No root')
            else:
                print(' ', 'root is ', result, ' ', result**power, '~=',x)

help(findroot)
testfindroot()

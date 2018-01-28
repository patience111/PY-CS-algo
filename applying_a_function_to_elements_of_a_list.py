import math
def applytoeach(L,F):
    '''Assume L is a list, f is a function MutatesL by replacing each element, e, of L by f(e)'''
    for i in range(len(L)):
        L[i]=F(L[i])

L=[1,-2,3.33]
print('L=',L)
print('Apply abs to each element of L.')
applytoeach(L,abs)
print('L=',L)
print('Apply int to each element of',L)
applytoeach(L,int)
print('L=',L)
print('Apply factorial to each element of',L)
applytoeach(L,math.factorial)
print('L=',L)


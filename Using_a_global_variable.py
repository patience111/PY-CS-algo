def fib(x):
    '''Assume x an int >=0 Returns Fibonacci of x'''
    global numFibcalls
    numFibcalls+=1
    if x==0 or x==1:
        return 1
    else:
        return fib(x-1)+fib(x-2)
def testFib(n):
    for i in range(n+1):
        global numFibcalls
        numFibcalls=0
        print('fib of',i,'=',fib(i))
        print('fib called',numFibcalls,'times.')
n=int(input('Please input a number n:'))
testFib(n)


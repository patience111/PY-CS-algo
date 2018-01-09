#Find x such that x**2-24 is within epsilon of 0
epsilon=0.01
k=25.0
guess=k/2.0
num=0
while abs(guess*guess-k)>=epsilon:
    guess=guess-(((guess**2)-k)/(2*guess))
    num=num+1
    print('This is the '+str(num)+' number guess and the guess number is '+ str(guess))
print('Square root of',k,' is about ',guess )



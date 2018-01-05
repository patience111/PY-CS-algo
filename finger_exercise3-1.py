x=int(input('please enter an integer:'))
pwr=1
while pwr<6:
    factorize=False
    if x%pwr==0:
        root=x/pwr
        print(str(x)+' can be factor by '+str(pwr)+' and '+str(root))
        factorize=True
    pwr=pwr+1
if factorize==False:
    print('no factors!')


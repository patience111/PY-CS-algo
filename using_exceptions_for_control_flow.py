def getRatio(vect1,vect2):
    '''Assume: vect1 and vect2 are equal length lists of numbers
       Return: a list containing the meaningful values of vect1[i]/vect2[i]'''
    ratios=[]
    for index in range(len(vect1)):
        try:
            ratios.append(vect1[index]/vect2[index])
        except ZeroDivisionError:
            ratios.append(float('nan'))
        except:
            raise ValueError('getRatios called with bad arguments')
    return ratios
value=getRatio([1.0,2.0,3.0,4.0],[2.0,3.0,4.0,0])
print(value)


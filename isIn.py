str1=input('please input a string:')
str2=input('please input another string:')
def isIn(s1,s2):
    if (s1 in s2) or (s2 in s1):
        return True
    else:
        return False
ans=isIn(str1,str2)
print(ans)

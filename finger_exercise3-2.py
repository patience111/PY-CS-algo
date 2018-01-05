s='1.23,2.4,3.123'
sum=0
for i in s:
    if i !='.' and  i !=',':
        sum=sum+int(i)

print(sum)

namehandle=open('kids','w')
namehandle.write('Micheal\n')
namehandle.write('Mark\n')
namehandle.close()
namehandle=open('kids','r')
for line in namehandle:
    print(line[:-1])
namehandle.close()
namehandle=open('kids','a')
namehandle.write('David\n')
namehandle.write('Andrea\n')
namehandle.close()
namehandle=open('kids','r')
for line in namehandle:
    print(line[:-1])

namehandle.close()


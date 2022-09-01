import os
os.chdir('D:\\')
l = os.listdir('D:\\')

for i in l:
    try:
        print 'D:\\'+i
        print os.listdir('D:\\'+i)
    except:
        print '\n'
        print 'None!!'
        print '\n'


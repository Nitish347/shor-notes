x1,y1,x2,y2,x3=float(input()),float(input()),float(input()),float(input()),float(input())
y3,b=0,1
if (x2-x1)!=0:
    y3=(((x3-x1)*(y2-y1))/(x2-x1)) + y1
    print(y3)
else:
    print('Vertical Line', end='')
    b=0
if (x2-x1)!=0:
    m=(y2-y1)/(x2-x1)
elif (x3-x2)!=0:
    m=(y3-y2)/(x3-x2)
elif (x3-x1)!=0:
    m=(y3-y1)/(x3-x1)
else:
    print('seems some mistake', end='')
if m == 0:
    print('Horizontal Line', end='')
elif m > 0 and b==1:
    print('Positive Slope', end='')
elif m < 0 and b==1:
    print('Negative Line', end='')

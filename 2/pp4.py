# Write your code here :-)
a=int(input('enter a valve:'))
b=int(input('enter b valve:'))
c=int(input('enter c valve:'))
if(a>b)and(a>c):
    print(a)
elif(b>a)and(b>c):
    print(b)
else:
    print(c)

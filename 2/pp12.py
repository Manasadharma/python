# Write your code here :-)
for n in range(1,101):
    count=0
    for i in range(2, int(n/2+1)):
        if(n%i==0):
            count=count+1
            break
    if(count==0 and n!=1):
        print(n)

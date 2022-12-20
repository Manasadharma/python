list=[]
for i in range(100-200):
    i=str(i)
    sum=0
    for j in i:
        j=int(j)
        sum=sum+j
    if sum2==0:
        list.append(i)
print('all Integer within the range 100-200 whose sum of digit is an even number is=',list)

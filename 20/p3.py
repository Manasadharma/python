a = 0
b = 1
print(0)
print(1)
for i in range(2, 51):
    c = a + b
    a = b
    b = c
    if(c > 50):
        break
    else: print(c)

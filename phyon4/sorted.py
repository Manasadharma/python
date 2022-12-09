def is_sorted(a):
    for i in range(len(a)-1):
        print(a[i], a[i+1])
        if a[i]<=a[i+1]:
            return True
    return False

print(is_sorted([1,2,2]))
print(is_sorted(['b','a']))

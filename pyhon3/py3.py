def num(lst):
    del lst[0]
    del lst[-1:]
def middle(lst):
    new = lst[1:]
    del new[-1:]
    return new
list1 = [1,2,3,4]
list2 = [1,2,3,4]
numlist = num(list1)
print(list1)
print(numlist)
middlelist = middle(list2)
print(list2)
print(middlelist)

l = [[1, 2], [3],[4, 5, 6,]]

def nested_sum(lst):

    sum = 0

    for i in lst:
        for j in i:
            sum = sum + j

    print(sum)


nested_sum(l)







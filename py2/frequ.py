import collections

L = [1, 2, 8, 5, 8, 7, 8]


largest = max(L)


res = collections.Counter(L)

print(res[largest])

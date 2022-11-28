test_list = ['abc', 1, 2, 'is', 'best']

print("The original list : " + str(test_list))

res_str = [ele for ele in test_list if isinstance(ele, str)]
res_int = [ele for ele in test_list if isinstance(ele, int)]

print("Integer list : " + str(res_int))
print("String list : " + str(res_str))

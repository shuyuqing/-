info_list = [['s'],['a'],['s'],['u'],['s'],['s'],['r']]

print(info_list)

n = 0
info_list_1 = info_list.copy()#这里用浅度拷贝的话就能找出其中的s
for item in info_list_1:  # 把逗号pop掉

    print(item[0])

    if item[0] == 's':
        print(n)
        info_list.pop(n)
        n = n-1

    n = n+1

print(info_list)

# info_list = [['s'],['a'],['s'],['u'],['s'],['s'],['r']]
#
# print(info_list)
#
# n = 0
# info_list_1 = info_list#直接这样用等号去赋值的话就不行
# for item in info_list_1:
#
#     print(item[0])
#
#     if item[0] == 's':
#         print(n)
#         info_list.pop(n)
#         n = n-1
#
#     n = n+1
#
# print(info_list)
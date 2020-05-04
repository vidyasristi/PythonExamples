from collections import OrderedDict

# test_list = [1, 5, 3, 6, 3, 5, 6, 1]
# test_list=input()
from os.path import split

#test_list = [int(x) for x in input().split()]
# print(test_list)
# res = list(OrderedDict.fromkeys(test_list))
# print("The original list is : " + str(test_list))
# print("The list after removing duplicates : " + str(res))
# print(len(res))
# [1,2,1,3]
# i = 0
#
# while i < len(test_list):
#     j = i + 1
#     while j < len(test_list):
#         if test_list[i] == test_list[j]:
#             del test_list[j]
#         else:
#             j += 1
#     i += 1
#
# print(test_list)




test_list = [int(x) for x in input().split()]
len_ = 1
if len(test_list)==0:
    print('0')
for i in range(1,len(test_list)):
    if test_list[i] != test_list[i-1]:
        test_list[len_] = test_list[i]
        len_ +=1
print(len_)

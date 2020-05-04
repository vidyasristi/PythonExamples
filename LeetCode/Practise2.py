a = [int(x) for x in input().split()]
new_list = []
for nums in a:
    if nums < 5:
        new_list.append(nums)

print(new_list)

"""
给定一维数组，要求找出数组中一个数，
使得该数等于左边之和同时也等于右边之和，如有多个仅输出第一个，
如果没有返回False
"""
nums = list(map(int, input().strip().split(',')))
sum = sum(nums)
find = sum/3
if find.is_integer():
    for item in nums:
        if item == int(find):
            print(item)
            break
else:
    print("False")


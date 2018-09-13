"""
2,2,4,7,7-1,2,3,5,6,9:6
"""
num_list, k = input().strip().split(':')
k = int(k)
nums = num_list.split('-')
num1 = list(map(int, nums[0].split(',')))
num2 = list(map(int, nums[1].split(',')))

num1.sort(reverse=True)
num2.sort(reverse=True)
count = 0
res = []
i = 1
j = 1
max1 = num1[0]
while num1[i] == max1:
    i += 1
max2 = num2[0]
while num2[j] == max2:
    j += 1
print(i, j)
num1 = [item+max2 for item in num1] * j
num2 = [item+max1 for item in num2[j:]] * i
num = num1+num2
num.sort(reverse=True)

print(','.join([str(item) for item in num[:k]]))

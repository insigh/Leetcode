"""
4
6 9
2 6
4 5
3 7
"""

n = int(input().strip())
time_line = []
for i in range(n):
    line = list(map(int, input().strip().split()))
    task = (line[0], line[1])
    time_line.append(task)
time_line.sort(key=lambda x:x[1])
end_time = 0
count = 0
for item in time_line:
    if item[0] < end_time:
        continue
    else:
        count += 1
        end_time = item[1]
print(count)

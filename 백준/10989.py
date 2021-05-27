from sys import stdin

N = int(stdin.readline())

nums = [0]*10001

for _ in range(N):
    nums[int(stdin.readline())] += 1

nums2 = []
for idx in range(N):
    temp = []
    if nums[idx] != 0:
        temp.append(idx)
        temp *= nums[idx]
        nums2 += temp

s = ""
for num in nums2:
    s += (str(num) + '\n')
print(s)
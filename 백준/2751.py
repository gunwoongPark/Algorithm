from sys import stdin

N = int(stdin.readline())

nums = [0] * N
for idx in range(N):
    nums[idx] = int(stdin.readline())

nums.sort()

s = ""
for num in nums:
    s += (str(num) + '\n')
print(s)
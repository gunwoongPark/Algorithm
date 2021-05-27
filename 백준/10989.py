from sys import stdin
from sys import stdout

N = int(stdin.readline())

nums = {str(i) : 0 for i in range(1, 10001)}

for _ in range(N):
    nums[stdin.readline()[:-1]] += 1

for key, val in nums.items():
    while val:
        stdout.write(key+"\n")
        val-=1
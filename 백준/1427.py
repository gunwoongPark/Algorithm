from sys import stdin

nums = list(map(int, stdin.readline()[:-1]))

nums.sort(reverse=True)

nums = list(map(str, nums))

print("".join(nums))
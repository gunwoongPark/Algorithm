K = int(input())

nums = []

for _ in range(K):
    nums.append(int(input()))

stack = []

for num in nums:
    if num == 0:
        stack.pop(-1)

    else:
        stack.append(num)

print(sum(stack))
N = int(input())

str_arr = [None] * N
for idx in range(N):
    str = input()
    str_arr[idx] = (str, len(str))

# print(str_arr)

str_arr = list(set(str_arr))

str_arr.sort(key=lambda str: (str[1], str[0]))

for str in str_arr:
    print(str[0])
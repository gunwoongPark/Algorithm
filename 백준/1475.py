from collections import Counter
import math

N = input()

count_of_num = Counter(N).most_common()

result = 0
num_of_69 = 0

for num in count_of_num:
    if num[0] == '6' or num[0] == '9':
        num_of_69 += num[1]
    else:
        result = num[1]
        break

print(max(math.ceil(num_of_69/2), result))
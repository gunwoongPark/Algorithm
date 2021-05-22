expression = input().split('-')
result = 0

for idx in expression[0].split('+'):
    result += int(idx)

for idx in expression[1:]:
    for jdx in idx.split("+"):
        result -= int(jdx)

print(result)
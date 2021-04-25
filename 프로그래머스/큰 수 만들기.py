def solution(number, k):
    stack = {}
    num_list = list(number)
    stack.append(num_list.pop(0))

    while True:
        if k == 0:
            break

        if len(stack) == 0:
            stack.append(num_list.pop(0))

        elif num_list[0] > stack[-1]:
            stack.pop(-1)
            k -= 1
        elif num_list[0] <= stack[-1]:
            stack.append(num_list.pop(0))


    answer = "".join(stack + num_list)

    return answer

print(solution("1231234", 3))
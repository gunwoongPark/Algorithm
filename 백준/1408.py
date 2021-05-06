cur_time = list(map(int,input().split(":")))
start_time = list(map(int,input().split(":")))

cur_time = cur_time[0]*3600 + cur_time[1]*60 + cur_time[2]
start_time = start_time[0]*3600 + start_time[1]*60 + start_time[2]
if start_time>=cur_time:
    result_time = start_time - cur_time
else :
    result_time = ((24*3600)+start_time)-cur_time

result_min, result_sec = divmod(result_time, 60)
result_hour, result_min = divmod(result_min, 60)

result= []
result.append(result_hour)
result.append(result_min)
result.append(result_sec)

answer = []
for el in result:
    if el < 10:
        answer.append('0'+str(el))
    else:
        answer.append(str(el))
print(":".join(answer))
h = int(input('h = '))
summary = []
list_of_indx = []
prev_idx = 0
for i in range(h):
    i+=1
    temp_list = []
    
    temp = input()
    temp_list = temp.split(' ')

    if len(temp_list) == 1 or (len(temp_list) > 1 and temp_list[prev_idx] < temp_list[prev_idx + 1]):
        list_of_indx.append(prev_idx)
    else:
        list_of_indx.append(prev_idx + 1)
        prev_idx += 1

    summary.append(temp_list)

result = []

for i in range(h):
    result.append(int(summary[i][list_of_indx[i]]))

print(sum(result))
print(*(i for i in result))


n, k = list(map(int, input('n k: ').split(' ')))

snow = [0] * n

for i in range(k):
    inp = list(map(int, input('номер операции, индекс улицы, мм снега/вторая улица: ').split(' ')))
    if inp[0] == 1:
        snow[inp[1] - 1] = inp[2]
    else:
        print(sum(snow[inp[1]: inp[2] + 1]))
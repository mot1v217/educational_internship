h = int(input('h = '))
triangle = []
for i in range(h):
    row = list(map(int, input().split()))
    triangle.append(row)
dp = [[val, [val]] for val in triangle[-1]]
for i in range(h - 2, -1, -1):
    new_dp = []
    for j in range(len(triangle[i])):
        if dp[j][0] <= dp[j + 1][0]:
            min_sum = dp[j][0]
            path = dp[j][1][:]
        else:
            min_sum = dp[j + 1][0]
            path = dp[j + 1][1][:]
        new_dp.append([triangle[i][j] + min_sum, [triangle[i][j]] + path])
    dp = new_dp
print(dp[0][0])
print(*dp[0][1])

n = int(input())
ls = list(map(int, input().split(" ")))
res = 0
dp_max = [[0] * n for i in range(n)]
dp_min = [[0] * n for i in range(n)]
dp_max[0] = ls
for i in range(n):
    if dp_max[0][i + 1] <= dp_max[0][i]:
        dp_max[0][i + 1] = dp_max[0][i]
    if dp_min[0][i + 1] >= dp_min[0][i]:
        dp_min[0][i + 1] = dp_min[0][i]
    dp_max[i][i]
for i in range(1,n):
    for j in range(i,n):
        if dp_max[i][0]>
print(res)

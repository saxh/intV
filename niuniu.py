s = input()
# print(s)
job = []
d = s.strip().split(" ")
d = [int(i) for i in d]
for i in range(d[0]):
    tmp = input().strip().split(" ")
    tmp = [int(i) for i in tmp]
    job.append(tmp)

ablity = []

ablity = input().strip().split(" ")
ablity = [int(i) for i in ablity]
# print(job)
# print(ablity)
job = sorted(job, reverse=True)
# print(job)
res = []
for i in range(d[1]):
    for j in range(d[0]):
        if job[j][0] <= ablity[i]:
            res.append(job[j][1])
            break
print(res)

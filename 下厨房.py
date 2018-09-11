# import sys
#
# res = set()
# while input():
#
#     tmp = input()
#     if tmp:
#         for a in tmp.split():
#             res.add(a)
#     else:
#         break
# print(len(res))
import sys

a = []
for line in sys.stdin:
    if line.strip() == '':
        break
    a.extend(line.split())
print(len(set(a)))

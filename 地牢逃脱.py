a = input().split(" ")
# 长宽
h = int(a[0])
w = int(a[1])
mat = [[0] * w for i in range(h)]
visited = [[False] * w for i in range(h)]
N = 0
for i in range(h):
    m = input()
    for j in range(w):
        mat[i][j] = m[j]
        if mat[i][j] != ".":
            visited[i][j] = True
        else:
            N += 1
# 初始位置
b = input().split(" ")
x0 = int(b[0])
y0 = int(b[1])
# 步子信息
c = int(input())
step_mat = [[0] * 2 for i in range(c)]
for i in range(c):
    step = input().split(" ")
    step_mat[i][0] = int(step[0])
    step_mat[i][1] = int(step[1])


def layer():
    q = [[x0, y0]]
    visited[x0][y0] = True
    step, count = 1, 1
    while q:
        tmp = []
        for i, j in q:
            for dx, dy in step_mat:
                nx, ny = dx + i, dy + j
                if 0 <= nx < h and 0 <= ny < w:
                    if visited[nx][ny] is False and mat[nx][ny] == ".":
                        tmp.append([nx, ny])
                        visited[nx][ny] = True
                        count += 1
                        if count == N:
                            return step
        q, step = tmp, step + 1
    return -1


if __name__ == '__main__':
    print(layer())

#0: 오른쪽, 1: 위쪽, 2: 왼쪽, 3: 아랫쪽
dxdy = [(0, 1), (-1, 0), (0, -1), (1, 0)]

#드래곤 커브의 개수
N = int(input())

points = set()
arr = [[0] * 100 for _ in range (100)]

for _ in range (N):
    x, y, d, G = map(int, input().split())
    dirs = [d]
    points.add((x, y))

    for g in range (G):
        new_dirs = []
        for i in range (len(dirs)):
            new_dirs.append((dirs[i] +1) % 4)
        dirs = dirs + new_dirs[::-1]

    for i in dirs:
        nx = x + dxdy[i][0]
        ny = y + dxdy[i][1]

        points.add((nx, ny))

        x = nx
        y = ny


for px, py in points:
    arr[px][py] = 1

cnt = 0
for px, py in points:
    if 0 <= px + 1 < 100 and 0 <= py +1 < 100:
        if arr[px][py+1] == 1 and arr[px+1][py] == 1 and arr[px+1][py+1] == 1:
            cnt += 1

print(cnt)
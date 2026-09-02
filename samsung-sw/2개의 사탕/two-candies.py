
didj = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def real_slide(way, r, c, other_r, other_c):
    while True:
        nr = r + didj[way][0]
        nc = c + didj[way][1]

        #가려는 길에 다른 사탕이 있는데 그게 도착지면 같이 가야됨.
        if nr == other_r and nc == other_c and arr[nr][nc] == 'O':
            r = nr
            c = nc
            break
        #가려는 길이 도착지가 아닌데 다른 사탕이 있으면 못 감.
        if nr == other_r and nc == other_c:
            break
        #가려는 길이 벽이 아님, 출구가 아님
        if arr[nr][nc] != '#' and arr[nr][nc] != 'O':
            r = nr
            c = nc
        #가는 길이 출구. 갑 업데이트 하고 보내기.
        elif arr[nr][nc] == 'O':
            r = nr
            c = nc
            break
        else:
            break

    return r, c


def slide_candy (way, rr, rc, br, bc):
    if way == 0:
        if rr <= br:
            rr, rc = real_slide(way, rr, rc, br, bc)
            br, bc = real_slide(way, br, bc, rr, rc)
        else:
            br, bc = real_slide(way, br, bc, rr, rc)
            rr, rc = real_slide(way, rr, rc, br, bc)
    if way == 1:
        if rr >= br:
            rr, rc = real_slide(way, rr, rc, br, bc)
            br, bc = real_slide(way, br, bc, rr, rc)
        else:
            br, bc = real_slide(way, br, bc, rr, rc)
            rr, rc = real_slide(way, rr, rc, br, bc)
    if way == 2:
        if rc <= bc:
            rr, rc = real_slide(way, rr, rc, br, bc)
            br, bc = real_slide(way, br, bc, rr, rc)
        else:
            br, bc = real_slide(way, br, bc, rr, rc)
            rr, rc = real_slide(way, rr, rc, br, bc)
    if way == 3:
        if rc >= bc:
            rr, rc = real_slide(way, rr, rc, br, bc)
            br, bc = real_slide(way, br, bc, rr, rc)
        else:
            br, bc = real_slide(way, br, bc, rr, rc)
            rr, rc = real_slide(way, rr, rc, br, bc)

    return rr, rc, br, bc



def backtracking(rr, rc, br, bc, n, way):

    global min_cnt

    if way != -1: #새로 좌표 받아온다.
        rr, rc, br, bc = slide_candy(way, rr, rc, br, bc)

    #종료조건:
    if n >= 11:
        min_cnt = min(min_cnt, n)
        return

    if arr[rr][rc] == 'O':
        if arr[br][bc] == 'O':
            return

        min_cnt = min(min_cnt, n)
        return

    if arr[br][bc] == 'O':
        return

    for i in range (0, 4):
        nrr = rr + didj[i][0]
        nrc = rc + didj[i][1]

        if arr[nrr][nrc] == '#':
            continue
        else:
            backtracking(rr, rc, br, bc, n+1, i)


N, M = map(int, input().split())

arr = [list(input().strip()) for _ in range (N)]

min_cnt = float("inf")

red_r, red_c = -1, -1
blue_r, blue_c = -1, -1

for i in range (N):
    for j in range (M):
        if arr[i][j] == 'R':
            red_r, red_c = i, j
            arr[i][j] = '.'
        elif arr[i][j] == 'B':
            blue_r, blue_c = i, j
            arr[i][j] = '.'

ways = []
backtracking(red_r, red_c, blue_r, blue_c, 0, -1)
# print(red_r, red_c)
# print(blue_r, blue_c)
# red_r, red_c, blue_r, blue_c = slide_candy (3, red_r, red_c, blue_r, blue_c)
# print(red_r, red_c)
# print(blue_r, blue_c)
# red_r, red_c, blue_r, blue_c = slide_candy (1, red_r, red_c, blue_r, blue_c)
# print(red_r, red_c)
# print(blue_r, blue_c)
# red_r, red_c, blue_r, blue_c = slide_candy (2, red_r, red_c, blue_r, blue_c)
# print(red_r, red_c)
# print(blue_r, blue_c)
# print(arr[red_r][red_c])
if min_cnt >= 11:
    print(-1)
else:
    print(min_cnt)
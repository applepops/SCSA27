#노랭이 구역 블록 내리기
def drop_in_yellow(yt, yx, yy):
    yx = -1 #사실상 x값은 안 쓴다.
    if yt == 1:
        for r in range(6):
            nx = yx + 1
            if yellow_visited[nx][yy] == 1:
                yellow_visited[yx][yy] = 1 #블록 넣어주기
                break
            else:
                yx = nx
        #끝까지 방해꾼이 없었다면 마지막라인에 들어간다.
        else:
            yellow_visited[yx][yy] = 1

    elif yt == 2:
        for r in range(6):
            nx = yx + 1
            #둘 중 하나라도 못 내려간다면..
            if yellow_visited[nx][yy] == 1 or yellow_visited[nx][yy+1] == 1:
                yellow_visited[yx][yy] = 1 #블록 넣어주기
                yellow_visited[yx][yy+1] = 1
                break
            else:
                yx = nx
        else:
            yellow_visited[yx][yy] = 1
            yellow_visited[yx][yy + 1] = 1
    elif yt == 3:
        for r in range(5):
            nx = yx + 1
            if yellow_visited[nx+1][yy] == 1:
                yellow_visited[yx][yy] = 1  # 블록 넣어주기
                yellow_visited[yx+1][yy] = 1
                break
            else:
                yx = nx
        else:
            yellow_visited[yx][yy] = 1
            yellow_visited[yx+1][yy] = 1



#빨갱이 구역 블록 내리기
def drop_in_red(rt, rx, ry):
    rx = -1
    if rt == 1:
        for r in range(6):
            nx = rx + 1
            if red_visited[nx][ry] == 1:
                red_visited[rx][ry] = 1 #블록 넣어주기
                break
            else:
                rx = nx
        else:
            red_visited[rx][ry] = 1

    elif rt == 2:
        for r in range (5):
            nx = rx + 1
            if red_visited[nx+1][ry] == 1:
                red_visited[rx][ry] = 1
                red_visited[rx+1][ry] = 1
                break
            else:
                rx = nx
        else:
            red_visited[rx][ry] = 1
            red_visited[rx + 1][ry] = 1

    elif rt == 3:
        for r in range(6):
            nx = rx + 1
            # 둘 중 하나라도 못 내려간다면..
            if red_visited[nx][ry] == 1 or red_visited[nx][ry + 1] == 1:
                red_visited[rx][ry] = 1  # 블록 넣어주기
                red_visited[rx][ry + 1] = 1
                break
            else:
                rx = nx
        else:
            red_visited[rx][ry] = 1
            red_visited[rx][ry + 1] = 1

#꽉 찬 경우 처리하는 함수
def check_full(arr):
    global points

    delete_row_lst = []
    for i in range (6):
        cnt = 0
        for j in range (4):
            if arr[i][j] == 1:
                cnt += 1
        #모든 애들이 다 1이면
        if cnt == 4:
            delete_row_lst.append(i)

    #혹시나 idx 달라지려나? 근데 위에서부터 순회해서 넣으니까 괜찮지 않을까?
    for r in delete_row_lst:
        arr = [[0, 0, 0, 0]] + arr[:r] + arr[r+1:]
        points += 1

    return arr


#연한 부분 처리하는 함수
def check_front(arr):
    global points

    flag0 = False
    flag1 = False
    for j in range(4):
        if arr[0][j] == 1:
            flag0 = True
            break
    for j in range(4):
        if arr[1][j] == 1:
            flag1 = True
            break

    if flag0:
        arr = [[0, 0, 0, 0]] + arr[:-1]

    if flag1:
        arr = [[0, 0, 0, 0]] + arr[:-1]

    return arr

#단위테스트용
def print_visited(arr):
    print("==============")
    for row in arr:
        print(*row)
    print("==============")

#입력받기
K = int(input())

#놀이판 만들어주기. 블록이 있으면 1이 들어가게.
red_visited = [[0] * 4 for _ in range (6)]
yellow_visited = [[0] * 4 for _ in range (6)]

points = 0

for k in range (K):
    t, x, y = map(int, input().split())

    #1. 블록 내리기
    drop_in_yellow(t, x, y)
    #빨갱이 블록 함수 부를 때는 x하고 y를 반대로 넣어주소.
    drop_in_red(t, y, x)

    #2. 꽉 찬 경우 처리
    yellow_visited = check_full(yellow_visited)
    red_visited = check_full(red_visited)

    #3. 연한 부분 처리
    yellow_visited = check_front(yellow_visited)
    red_visited = check_front(red_visited)


# print_visited(yellow_visited)
# print_visited(red_visited)

remained_cnt = 0
for i in range (6):
    for j in range (4):
        if yellow_visited[i][j] == 1:
            remained_cnt+= 1
        if red_visited[i][j] == 1:
            remained_cnt+= 1


print(points)
print(remained_cnt)
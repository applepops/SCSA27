#주사위 움직이게 하는 함수. 움직여야 하는 방향을 받는다.
def move(c_dir): #위, 아래, 왼, 오른, 앞, 뒤
    if c_dir == 1:#동
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[2], dice[3], dice[1], dice[0], dice[4], dice[5]
    elif c_dir == 2:#서
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[3], dice[2], dice[0], dice[1], dice[4], dice[5]
    elif c_dir == 3:#님
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[4], dice[5], dice[2], dice[3], dice[1], dice[0]
    elif c_dir == 4:#북
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[5], dice[4], dice[2], dice[3], dice[0], dice[1]

def print_arr():
    print("=============")
    for row in arr:
        print(*row)

#방향 벡터 -> 딕셔너리로
#순서대로 동, 서, 북, 남
didj = {1: (0, 1), 2:(0, -1), 3:(-1, 0), 4:(1, 0)}

#입력받기
N, M, x, y, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range (N)]
ways = list(map(int, input().split()))

#주사위 초기화
dice = [0] * 6

#현재 위치 초기화
ci = x
cj = y

for c_way in ways:

    ni = ci + didj.get(c_way, 0)[0]
    nj = cj + didj.get(c_way, 0)[1]

    #주사위 다음 위치 범위 확인. 범위 나가면 무시.
    if not (0 <= ni < N and 0 <= nj < M):
        continue

    ci = ni #주사위 위치 업데이트
    cj = nj

    move(c_way)
    if arr[ci][cj] == 0:
        arr[ci][cj] = dice[1]
    elif arr[ci][cj] != 0:
        dice[1] = arr[ci][cj]
        arr[ci][cj] = 0

    print(dice[0])

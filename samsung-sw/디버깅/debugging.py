def down_ladder(guest_num):

    for row in range (0, H):

        if guest_num == 0:
            if arr[row][guest_num] == 1:
                guest_num += 1
        elif guest_num == N-1:
            if arr[row][guest_num-1] == 1:
                guest_num -= 1
        else:
            if arr[row][guest_num] == 1:
                guest_num += 1
            elif arr[row][guest_num-1] == 1:
                guest_num -= 1

    return guest_num

def backtracking(n, kigun_n):

    if n == kigun_n:

        is_fixed = True
        for guest in range (N):
            if guest != down_ladder(guest):
                is_fixed = False

        if is_fixed:
            # print()
            # for row in arr:
            #     print(*row)
            print(kigun_n)
            exit()

        else:
            return False

    for i in range (H):
        for j in range(N - 1):
            if arr[i][j] == 0:
                arr[i][j] = 1
                backtracking(n+1, kigun_n)
                arr[i][j] = 0

def call_backtracking():

    backtracking(0, 0)

    backtracking(0, 1)

    backtracking(0, 2)

    backtracking(0, 3)

    print(-1)
    exit()

#고객 수, 메모리 유실 선 수, 취약지점 개수
N, M, H = map(int, input().split()) #[주의] row가 M인줄.. 실수..

arr = [[0] * N for _ in range (H)]

for _ in range (M):
    a, b = map(lambda x: int(x)-1, input().split())

    arr[a][b] = 1


if M == 0:
    print(0)
else:
    call_backtracking()


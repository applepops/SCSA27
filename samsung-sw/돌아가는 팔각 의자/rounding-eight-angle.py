from collections import deque

#[입력받기]
arr = [[] for _ in range (4)]
for i in range (4):
    tmp = map(int, list(input()))
    arr[i] = deque(tmp)

K = int(input()) #회전 횟수

for k in range (K):

    #[1] 명령 받기
    n, d = map(int, input().split())
    n -= 1 #0-based로 만들어주기

    #[2] 회전 여부 확인
    does_move = [0, 0, 0, 0]
    does_move[n] = d #움직여야 하는 애 먼저 업데이트

    #[2.1] 왼쪽으로 연쇄 반응
    for i in range (n-1, -1, -1):
        if does_move[i+1] != 0 and arr[i][2] != arr[i+1][-2]:
            does_move[i] = does_move[i+1] * -1
        else:
            break

    #[2.2] 오른쪽으로 연쇄 반응
    for i in range(n+1, 4):
        if does_move[i-1] != 0 and arr[i][-2] != arr[i-1][2]:
            does_move[i] = does_move[i - 1] * -1
        else:
            break


    #[3] 돌리기
    for i in range (4):
        if does_move[i] == 0:
            continue
        else:
            if does_move[i] == 1:
                arr[i].rotate(1)
            else:
                arr[i].rotate(-1)

#[4] 출력 계산
ans = 0
score = [1, 2, 4, 8]
for i in range (4):
    if arr[i][0] == 1:
        ans += score[i]

print(ans)

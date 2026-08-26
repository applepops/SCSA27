#각 방향마다 더해줘야 하는 di/dj/비율 (마지막이 a%들어가는 위치임)
directions = {0: [(0, -2, 0.05), (-1, -1, 0.1), (1, -1, 0.1), (-1, 0, 0.07), (1, 0, 0.07), (-2, 0, 0.02), (2, 0, 0.02), (-1, 1, 0.01), (1, 1, 0.01), (0, -1, 0)],
              2: [(0, 2, 0.05), (-1, 1, 0.1), (1, 1, 0.1), (-1, 0, 0.07), (1, 0, 0.07), (-2, 0, 0.02), (2, 0, 0.02), (-1, -1, 0.01), (1, -1, 0.01), (0, 1, 0)],
              3: [(-2, 0, 0.05), (-1, -1, 0.1), (-1, 1, 0.1), (0, -1, 0.07), (0, 1, 0.07), (0, -2, 0.02), (0, 2, 0.02), (1, -1, 0.01), (1, 1, 0.01), (-1, 0, 0)],
              1: [(2, 0, 0.05), (1, -1, 0.1), (1, 1, 0.1), (0, -1, 0.07), (0, 1, 0.07), (0, -2, 0.02), (0, 2, 0.02), (-1, -1, 0.01), (-1, 1, 0.01), (1, 0, 0)]
              }

#좌 아래 우 위 순서
didj = [(0, -1), (1, 0), (0, 1), (-1, 0)]

#디버깅용 함수
def print_dusts():
    for row in arr:
        print(*row)

def add_dust(i, j, cur_dir):
    global out_dust

    cur_total_dust = 0

    for di, dj, p in directions.get(cur_dir, []):
        ni = i + di
        nj = j + dj

        # 마지막 a% 계산해주기
        if p == 0:
            if 0 <= ni < N and 0 <= nj < N:
                arr[ni][nj] += arr[i][j] - cur_total_dust
            else:
                out_dust += arr[i][j] - cur_total_dust

        else:
            temp_dust = int(arr[i][j] * p)
            cur_total_dust += temp_dust

            #다음 위치가 먼지를 더해줄 수 있는 곳이면
            if 0 <= ni < N and 0 <= nj < N:
                arr[ni][nj] += temp_dust
            #다음 위치가 먼지를 더해줄 수 없는 곳에 있으면
            else:
                out_dust += temp_dust



#격자의 크기
N = int(input())

arr = [list(map(int, input().split())) for _ in range (N)]

#청소를 시작하는 초기 위치
cur_i, cur_j = N //2, N // 2
#1만큼 가는 걸 2번.. 2만큼 가는 걸 2번...3만큼 가는 걸 2번...
#n번 가는 것이 2번씩 반복되는 패턴 + 다 가면 방향 바꾸기
how_much_far_i_go = 1

#초기 청소기 방향은 왼쪽
#맨 처음 위치는 먼지 없음
cur_dir = 0

#탈출 플래그
is_break = False

#격자밖으로 떨어져 나가는 먼지들 담는 변수
out_dust = 0

while True:
    for _ in range(2):
        for _ in range(how_much_far_i_go):
            cur_i += didj[cur_dir][0]
            cur_j += didj[cur_dir][1]

            add_dust(cur_i, cur_j, cur_dir)
            #그 자리 먼지 청소하기
            arr[cur_i][cur_j] = 0

            if cur_i == 0 and cur_j == 0:
                is_break = True
                break

        cur_dir = (cur_dir + 1) % 4

        if is_break:
            break

    how_much_far_i_go += 1
    if is_break:
        break

print(out_dust)

def push_pizza():
    global arr

    arr_0 = [row[:] for row in arr[:]]
    visited = [row[:] for row in arr[:]]
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            arr_0[i][j] = 0
            visited[i][j] = 0

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            visited[i][j] = 1

            for di, dj in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                ni = i + di
                nj = j + dj

                if 0 <= ni < len(arr) and 0 <= nj < len(arr[ni]) and visited[ni][nj] != 0:
                    d = abs(arr[i][j] - arr[ni][nj]) // 5
                    if arr[i][j] >= arr[ni][nj]:
                        arr_0[i][j] -= d
                        arr_0[ni][nj] += d
                    else:
                        arr_0[i][j] += d
                        arr_0[ni][nj] -= d

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            arr[i][j] += arr_0[i][j]

def flatten_pizza():
    global arr

    arr = [list(row) for row in zip(*arr[::-1])] + [arr[-1][len(arr[0]):]]
    flattened_arr = []
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            flattened_arr.append(arr[i][j])

    return flattened_arr


#나는 이미 풀었다.
#문제를 다 이해하기 전까지 생각 금지
#잊을만한 애들은 미리 주석으로 다 써두기

#입력받기
N, K = map(int, input().split())
arr = list(map(int, input().split()))

turn = 0 #횟수

#끝없이.. 반복할거야..
while True:
    #0. 밀가루 양의 최댓값과 최솟값을 알아온다. -> 엣지. 처리 안했지만 이미 K이하인 경우
    #0.1 그 차이가 K 이하면 break 아니면 계속 반복.
    max_milraru = max(arr)
    min_milraru = min(arr)
    if max_milraru - min_milraru <= K:
        break

    #0.2 횟수 += 1
    turn += 1

    #1. 밀가루 양이 가장 작은 위치에 밀가루를 1만큼 더 넣는다. (모든 가장 작은 위치에 다)
    for i in range (len(arr)):
        if arr[i] == min_milraru:
            arr[i] += 1

    #여기서부터 arr은 2차원 상태로.
    arr = [arr]
    #2.도우를 말아준다.
    tmp_lst = [] #슬라이싱으로 빼와야할 것 같음.

    c = 1
    while True:

        for i in range (len(arr)):
            tmp_lst.append(arr[i][:c])
            for _ in range (c):
                arr[i].pop(0)

        tmp_lst = [list(row) for row in zip(*tmp_lst[::-1])] #시계방향으로 돌려서 넣기

        arr = tmp_lst + [arr[-1]]
        c = len(arr[0])
        tmp_lst = [] #비워주기

        if len(arr) > len(arr[-1])-2:
            break


    #3. 도우를 꾹 눌러준다. (동시에 진행.)
    # 모든 좌표들을 돌면서 따로 추가 혹은 빼주는 배열 만들어서 거기에 저장해두고 한꺼번에 연산.
    push_pizza()

    #4. 한줄로 쭉 핀다. 열이 작은 것 그리고 행이 큰 순서로.
    #flatten된 상태.
    flattened_arr = flatten_pizza()


    #5. 도우를 두 번 반으로 접는다.

    #한 번 접었다.
    tmp_arr = []
    tmp_arr.append(flattened_arr[0:len(flattened_arr)//2][::-1])
    tmp_arr.append(flattened_arr[len(flattened_arr)//2:])

    cur_len = len(tmp_arr[0])

    for i in range(len(tmp_arr)):
        tmp_lst.append(tmp_arr[i][:cur_len//2])
        for _ in range(cur_len//2):
            tmp_arr[i].pop(0)

    tmp_lst = [list(row) for row in zip(*tmp_lst[::-1])]
    tmp_lst = [list(row) for row in zip(*tmp_lst[::-1])]

    arr = tmp_lst + tmp_arr

    #6. 도우를 꾹 눌러주는 거 한 번 더
    push_pizza()

    # #7. 한줄로 쭉 핀다. 열이 작은 것 그리고 행이 큰 순서로.
    arr = flatten_pizza()
    #flatten된 상태.

print(turn)
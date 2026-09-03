#너무 하기 싫은 마음을 이겨내야해!!!!!!!

#격자 크기, 플레이어 수, 독점계약턴 수
N, M, K = map(int, input().split())

#현재 격자 상태 입력받기
arr = [list(map(int, input().split())) for _ in range (N)]

didj = [(-1, 0), (1, 0), (0, -1), (0, 1)] #위아래왼오른

player_info = [[] for _ in range (M+1)] #플레이어 현재 위치 정보, 현재 방향 정보 저장 -> 가변, 1-based
player_dir_priority = dict() #플레이어마다의 방향별 우선순위 저장 -> 불변
cur_monopoly_state = dict() #좌표가 key, value는 [플레이어, 남은 독점계약 년수]

#현재 남은 플레이어를 담는 list, 초기값은 M명 다 있는 것.
cur_players = []
for i in range (1, M+1):
    cur_players.append(i)

#현재 위치 입력받기
for i in range (N):
    for j in range (N):
        if arr[i][j] != 0:
            player_info[arr[i][j]].append(i)
            player_info[arr[i][j]].append(j)
            cur_monopoly_state[(i, j)] = [arr[i][j], K]

#현재 바라보는 방향 입력받기
lst = list(map(int, input().split()))
for i in range (len(lst)):
    player_info[i+1].append(lst[i]-1)

#방향별 우선순위 방향 입력받기
for i in range (1, M+1):
    total_d = []
    for _ in range (4):
        d = list(map(lambda x : int(x) - 1, input().split())) #0-based로 위치 좌표 받을 거임.
        total_d.append(d)
    player_dir_priority[i] = total_d

turn = 0

while True:
    turn += 1

    if turn >= 1000:
        print(-1)
        exit()

    tmp_location = dict() #다 들어가고 나면 나중에 싹 넣어줄거임.

    # 2. 플레이어들의 이동
    #현재 남아있는 player들만큼만 반복하면 된다.
    for p in cur_players:
        next_location = [] #p가 가야 하는 다음 장소를 담자. 새로운 방향까지.

        cur_i, cur_j, cur_dir = player_info[p][0], player_info[p][1], player_info[p][2]

        # 2.1 빈자리가 있는지 확인
        for d in player_dir_priority[p][cur_dir]:
            ni = didj[d][0] + cur_i
            nj = didj[d][1] + cur_j

            if 0 <= ni < N and 0 <= nj < N:
                if not (ni, nj) in cur_monopoly_state.keys() or not cur_monopoly_state[(ni, nj)]:
                    next_location = [ni, nj, d]
                    break

        #2.2 없다면 내가 독점계약한 땅으로 이동
        if not next_location: #빈 리스트면..

            for d in player_dir_priority[p][cur_dir]:
                ni = didj[d][0] + cur_i
                nj = didj[d][1] + cur_j

                if 0 <= ni < N and 0 <= nj < N:

                    if cur_monopoly_state[(ni, nj)][0] == p:
                        next_location = [ni, nj, d]
                        break

        # 2.3 tmp_monopoly_state에다가 집어넣는다. 이미 있으면? 작은 애만 산다. 없으면? 들어간다.
        if next_location:
            #이미 들어간 녀석이 있구나.
            if (next_location[0], next_location[1]) in tmp_location.keys():
                if tmp_location[(next_location[0], next_location[1])] > p: #새로 들어가는 숫자가 더 작은 경우만 갱신.
                    player_info[p][0] = next_location[0] #이때 player_info도 update
                    player_info[p][1] = next_location[1]
                    player_info[p][2] = next_location[2]
                    tmp_location[(next_location[0], next_location[1])] = p
            #아무도 없었다..
            else:
                tmp_location[(next_location[0], next_location[1])] = p
                player_info[p][0] = next_location[0]  # 이때 player_info도 update
                player_info[p][1] = next_location[1]
                player_info[p][2] = next_location[2]

    #1.독점계약 년수가 1씩 줄어든다. -> 자리를 옮겨보자.
    for (i, j) in cur_monopoly_state.keys():
        if cur_monopoly_state[(i, j)]:
            cur_monopoly_state[(i, j)][1] -= 1
            if cur_monopoly_state[(i, j)][1] == 0: #독점계약 년수가 다 닳았다면.
                cur_monopoly_state[(i, j)].clear() #value를 빈 값으로 만든다. 어떻게 아예 지우는지는 모르겠음;;

    #3. cur_monopoly_state 갱신한다, 독점계약턴도 싹 넣어주고.
    for (ki, kj) in tmp_location.keys():
        cur_monopoly_state[(ki, kj)] = [tmp_location[(ki, kj)], K]



    #4. 남아있는 player들을 갱신한다. cur_player 갱신
    cur_players = list(tmp_location.values())


    if len(cur_players) == 1:
        print(turn)
        exit()


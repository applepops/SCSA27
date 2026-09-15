#제출 후 실패시 30분 뒤에 제출 가능함.
#신중한 단위테스트와 검증
#ideation 작은 과정도 꼼꼼하게 하기.

def find_moving_knights(lst, d):

    m_knights = set()

    for n in range (N):
        if dead_knights[n]: #이미 없어진 기사면 pass
            continue
        else:
            tmp_ijs = []
            if d in [0, 2]: #col 확인
                for j in range(knights_info[n][1], knights_info[n][1] + knights_info[n][3]):
                    tmp_ijs.append(j)
            else:           #row 확인
                for i in range(knights_info[n][0], knights_info[n][0] + knights_info[n][2]):
                    tmp_ijs.append(i)

            for ij in tmp_ijs:
                if ij in lst:
                    m_knights.add(n)

    return list(m_knights)

def can_we_move(m_knights, d): #움직이는 대상 좌표가 격자 밖이거나 벽이면 False 반환
    for k in m_knights:
        if d == 0:
            for i in range (knights_info[k][0]-1, knights_info[k][0]-1 + knights_info[k][2]):
                for j in range (knights_info[k][1], knights_info[k][1] + knights_info[k][3]):
                    if not 0 <= i < L or not 0 <= j < L:
                        return False
                    if arr[i][j] == 2:
                        return False
        elif d == 1:
            for i in range(knights_info[k][0], knights_info[k][0] + knights_info[k][2]):
                for j in range(knights_info[k][1]+1, knights_info[k][1]+1 + knights_info[k][3]):
                    if not 0 <= i < L or not 0 <= j < L:
                        return False
                    if arr[i][j] == 2:
                        return False
        elif d == 2:
            for i in range(knights_info[k][0] + 1, knights_info[k][0] + 1 + knights_info[k][2]):
                for j in range(knights_info[k][1], knights_info[k][1] + knights_info[k][3]):
                    if not 0 <= i < L or not 0 <= j < L:
                        return False
                    if arr[i][j] == 2:
                        return False
        elif d == 3:
            for i in range(knights_info[k][0], knights_info[k][0] + knights_info[k][2]):
                for j in range(knights_info[k][1] - 1, knights_info[k][1] - 1 + knights_info[k][3]):
                    if not 0 <= i < L or not 0 <= j < L:
                        return False
                    if arr[i][j] == 2:
                        return False
    else:
        return True #아무 문제도 없는 경우만 True 반환

#[입력받기]
#체크판 크기, 기사들 숫자, 명령 개수
L, N, Q = map(int, input().split()) #[주의] 체스판 L임

arr = [list(map(int, input().split())) for _ in range (L)] #불변

knights_info = []
for _ in range (N):
    r, c, h, w, k = map(int, input().split())
    r, c = r-1, c-1
    knights_info.append([r, c, h, w, k])

dead_knights = [False] * N
hurts_knights = [0] * N

#왕이 내린 명령만큼 돈다..
for q in range (Q):
    knight_num, way = map(int, input().split())
    knight_num -= 1

    #[1] 이미 사라진 기사를 움직이려고 하는가?
    if dead_knights[knight_num]:
        continue
    else:
        need_to_check_ij = []
        #아직 남아있는 기사다.

        #[2] 이 기사가 차지하고 있는 row 혹은 col을 알아내자.
        if way in [0, 2]: #col 확인
            for j in range (knights_info[knight_num][1], knights_info[knight_num][1] + knights_info[knight_num][3]):
                need_to_check_ij.append(j)
        else:             #row 확인
            for i in range(knights_info[knight_num][0], knights_info[knight_num][0] + knights_info[knight_num][2]):
                need_to_check_ij.append(i)

        #[3] 움직임의 대상이 되는 기사들을 알아오자.
        moving_knights = find_moving_knights(need_to_check_ij, way)

        #[4] 이번 이동이 가능한지 check한다.
        if can_we_move(moving_knights, way):
            # print("True")
            #[5] 기사들 위치를 업데이트 해준다.
            for m in moving_knights:
                if way == 0:
                    knights_info[m][0] -= 1
                elif way == 1:
                    knights_info[m][1] += 1
                elif way == 2:
                    knights_info[m][0] += 1
                elif way == 3:
                    knights_info[m][1] -= 1

            #[6] 데미지를 계산해서 업데이트 해준다.
            for m in moving_knights:
                if m == knight_num: #[주의] 명령을 받은 기사는 피해를 입지 않는다.
                    continue
                for i in range(knights_info[m][0], knights_info[m][0] + knights_info[m][2]):
                    for j in range(knights_info[m][1], knights_info[m][1] + knights_info[m][3]):
                        if arr[i][j] == 1: #함정이다
                            knights_info[m][4] -= 1
                            hurts_knights[m] += 1 #정보 업데이트

                            # [6.1] 사라진 기사인지도 확인해서 업데이트해준다.
                            if knights_info[m][4] <= 0:
                                dead_knights[m] = True #정보 업데이트
            # print(hurts_knights)
            # print(dead_knights)

        else: #이동이 불가능하다. 그냥 넘어간다.
            # print("False")
            continue


#[7] 생존한 기사들의 데미지를 더하자.
ans = 0
for n in range (N):
    if not dead_knights[n]: #살아있는 애들일 때만 더해라.
        ans += hurts_knights[n]

print(ans)
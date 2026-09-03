#말 움직이는 함수
def move(start, line_num, kan):
    past_line_num = line_num
    if start == 10:
        line_num = 10 #라인 업데이트
    elif start == 20:
        line_num = 20
    elif start == 30 and line_num == 0: #[주의]
        line_num = 30

    cur_line = lines.get(line_num, 0)

    if start == 30 and line_num == 30 and past_line_num == 30: #여기도 꼬인다. 한 라인에 같은 숫자가 두 개. 뒷 30 찾아가는 분기문
        cur_idx = 5
    else:
        cur_idx = cur_line.index(start)


    if cur_idx + kan >= len(cur_line):
        return 45, line_num
    else:
        return cur_line[cur_idx + kan], line_num


def backtracking(n, horse_positions, horse_lines, cur_score):
    global max_score

    #종료조건
    if n == 10:
        if max_score < cur_score:
            max_score = cur_score

        return

    #이번 턴에 고를 말의 번호를 돌자.
    for i in range (0, 4):

        #이미 도착지에 도착한 말인 경우
        if horse_positions[i] == 45:
            continue

        #말 한 번 이동시켜보자.
        res_position, res_line = move(horse_positions[i], horse_lines[i], kans[n])

        #도착칸에 도착한 거임.
        if res_position == 45:
            #깊은 복사
            new_horse_positions = horse_positions[:]
            new_horse_positions[i] = res_position #값 업데이트
            new_horse_lines = horse_lines[:]
            new_horse_lines[i] = res_line

            lst.append(i)
            backtracking(n + 1, new_horse_positions, new_horse_lines, cur_score) #도착칸이니까 점수 더하지 않는다.
            lst.pop()

        #도착칸이 아닌 어딘가에 도착했음.
        else:
            cnt = 0
            for h in range (4):
                if h == i:
                    continue
                # [주의] 여러 라인에 같은 위치가 있는 경우, 하나밖에 없는 숫자들이라서 두 개 이상은 무조건 문제된다.
                if res_position in [25, 35, 40] and res_position == horse_positions[h]:
                     cnt += 1
                # 30은 특별관리가 필요하다. 10줄에서 온 30, 20줄에서 온 30, 30줄에서 온 30과 0줄에서 지나가는 다른 30.
                if res_position == horse_positions[h] == 30 and res_line in [10, 20, 30] and horse_lines[h] in [10, 20, 30]:
                    cnt += 1
                # 겹치는 경우 [주의] 라인별로 같은 숫자지만 다른 위치 있어서 이것도 따져야 됨.
                if res_position == horse_positions[h] and res_line == horse_lines[h]:
                    cnt += 1

            #안 겹쳐야지만 백트래킹 부른다.
            if cnt == 0:
                #깊은 복사
                new_horse_positions = horse_positions[:]
                new_horse_positions[i] = res_position  # 값 업데이트
                new_horse_lines = horse_lines[:]
                new_horse_lines[i] = res_line
                lst.append(i)
                backtracking(n + 1, new_horse_positions, new_horse_lines, cur_score + res_position)
                lst.pop()
            else:
                continue


#이동 칸 수들 입력 받기 idx는 0부터 9로
kans = list(map(int, input().split()))
#초기값 설정

h_positions = [0, 0, 0, 0] #말들이 있는 번호
h_lines = [0, 0, 0, 0] #말들이 타고 있는 라인

max_score = 0

#출발칸하고 도착칸은 0, 45로 임의지정하겠음
lines = {0: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 45],
         10: [10, 13, 16, 19, 25, 30, 35, 40, 45],
         20: [20, 22, 24, 25, 30, 35, 40, 45],
         30: [30, 28, 27, 26, 25, 30, 35, 40, 45]}

lst = []
backtracking(0, h_positions[:], h_lines[:], 0)
print(max_score)


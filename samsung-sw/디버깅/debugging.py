def check_no_bug(lst):
    #모든 고객 명수만큼 반복한다.
    for c in range (1, N+1):
        cur_line = 0
        cur_customer = c
        #마지막 줄로 도착할 때까지
        while cur_line < M+1:
            #연결된 버그라인들 중에 cur_line보다 작거나 같은데 출발고객 같으면, 아니면 도착고객이 같으면..
            for l, sc in lst:
                if l >= cur_line:
                    #오른쪽으로 이동
                    if sc == cur_customer:
                        cur_customer = sc+1
                        cur_line = l
                    #왼쪽으로 이동
                    elif sc+1 == cur_customer:
                        cur_customer = sc
                        cur_line = l
                else:
                    cur_line += 1
            #연결된 버그라인에 갈만한 곳이 없으면 그냥 내려가야지.
            else:
                cur_line+=1
        if cur_customer == c:
            continue
        else:
            return False
    else:
        return True

def backtracking(n, start_idx, target):
    if n == target:
        tmp_tmp_lst = sorted(tmp_lst, key=lambda x: x[0])

        if check_no_bug(tmp_tmp_lst):
            print(target)
            exit()

        return

    for i in range(start_idx, len(fix_bug_lines_hubo)):
        tmp_lst.append(fix_bug_lines_hubo[i])
        backtracking(n + 1, i + 1, target)
        tmp_lst.pop()






#고객의 수(세로선 개수), 메모리 유실 선의 개수(버그 개수), 취약 지점의 개수(가로선 개수)
N, M, H = map(int, input().split())

#튜플로 버그 가로선 넘버랑 출발고객 넘버 (도착넘버는 start_cus_num+1)이긴 함 근데 서로 갈 수 있긴 함..
bug_lines = []
for _ in range (M):
    line_num, start_cus_num = map(int, input().split())
    bug_lines.append((line_num, start_cus_num))

#늘 정렬해야해..
bug_lines = sorted(bug_lines, key=lambda x: x[0])

fix_bug_lines_hubo = []
for i in range (1, H+1):
    #N번째 고객은.. 연결 선이 없으니까..
    for j in range (1, N):
        fix_bug_lines_hubo.append((i, j))

#후보들에서 못 가는 애들 지워주는 과정..
#메모리 유실선을 추가할 때 선이 겹치면 안된다고 했기에..
for line_num, start_cus_num in fix_bug_lines_hubo:
    for r_ln, r_scn in bug_lines:
        if line_num == r_ln and start_cus_num == r_scn:
            fix_bug_lines_hubo.remove((line_num, start_cus_num))
            if start_cus_num + 1 <= N-1:
                fix_bug_lines_hubo.remove((line_num, start_cus_num+1))
            if start_cus_num - 1 >= 1:
                fix_bug_lines_hubo.remove((line_num, start_cus_num-1))

#0번으로 해결가능한지 확인하자.
if check_no_bug(bug_lines):
    print(0)
    exit()

tmp_lst = [row[:] for row in bug_lines[:]]

for target in range(1, 4):
    backtracking(0, 0, target)


print(-1)


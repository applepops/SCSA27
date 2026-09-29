def gravity():

    global arr
    arr = [[0] * N for _ in range (N)]

    for k in box_order:
        cr, cc, ch, cw = box_info[k]

        for i in range (0, N-ch+1):
            tmp_arr = [row[cc:cc+cw] for row in arr[i+1:i+1+ch]]
            if sum(map(sum, tmp_arr)) == 0:
                continue
            else:
                break

        box_info[k][0] = i #row 정보 업데이트
        for r in range (i, i+ch):
            for c in range (cc, cc+cw):
                arr[r][c] = k

def check_end():
    if len(box_info) == 0:
        return True
    else: return False

def remove_box(box_num):
    cr, cc, ch, cw = box_info[box_num]
    for i in range(cr, cr + ch):
        for j in range(cc, cc + cw):
            arr[i][j] = 0

#[입력받기]###########################
N, M = map(int, input().split())
box_info = dict()
box_order = []
arr = [[0] * N for _ in range (N)]

for _ in range (M):
    k, h, w, c =map(int, input().split())
    c -= 1
    box_info[k] = [0, c, h, w]
    box_order.append(k)

####################################

#[실행부]############################
#[1] 택배 내리기
gravity()

# print("처음")
# for row in arr:
#     print(*row)

while True:
    #[2] 좌측 택배 하차
    can_move_left_lst = []
    for k in box_info.keys():
        cr, cc, ch, cw = box_info[k]
        tmp_space = [row[0:cc] for row in arr[cr:cr+ch]]

        if sum(map(sum, tmp_space)) == 0:
            can_move_left_lst.append(k)

    can_move_left_lst.sort()
    remove_box(can_move_left_lst[0])
    box_info.pop(can_move_left_lst[0])
    box_order.remove(can_move_left_lst[0])
    print(can_move_left_lst[0])

    gravity()

    # print("좌측 택배 하차 후")
    # for row in arr:
    #     print(*row)

    if check_end():
        break

    #[3] 우측 택배 하차
    can_move_right_lst = []
    for k in box_info.keys():
        cr, cc, ch, cw = box_info[k]
        tmp_space = [row[cc+cw:N] for row in arr[cr:cr+ch]]

        if sum(map(sum, tmp_space)) == 0:
            can_move_right_lst.append(k)

    can_move_right_lst.sort()
    remove_box(can_move_right_lst[0])
    box_info.pop(can_move_right_lst[0])
    box_order.remove(can_move_right_lst[0])
    print(can_move_right_lst[0])

    gravity()

    # print("우측 택배 하차 후")
    # for row in arr:
    #     print(*row)

    if check_end():
        break


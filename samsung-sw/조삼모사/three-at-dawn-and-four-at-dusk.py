def backtracking(n, start_idx):
    global min_workload

    if n == N/2:
        #저녁에 하는 일이 자동으로 정해지니까.
        evening_works = total_works - set(morning_works)
        evening_works = list(evening_works)

        temp_m = 0
        temp_e = 0

        #일의 강도 계산 때리기:
        for i in range (0, N//2-1):
            for j in range (i+1, N//2):
                temp_m += arr[morning_works[i]][morning_works[j]]
                temp_m += arr[morning_works[j]][morning_works[i]]
                temp_e += arr[evening_works[i]][evening_works[j]]
                temp_e += arr[evening_works[j]][evening_works[i]]

        min_workload = min(abs(temp_e - temp_m), min_workload)
        return

    for i in range (start_idx, N):
        morning_works.append(i)
        backtracking(n+1, i+1)
        morning_works.pop()



#총 N개의 일. 아침 저녁 N/2개로 나눠야 함.
N = int(input())
#일의 index는 0부터 N-1까지
arr = [list(map(int, input().split())) for _ in range (N)]

total_works = set()
for i in range (N):
    total_works.add(i)

morning_works = []
evening_works = []

min_workload = float("INF")
#일 개수 카운트, start_idx
backtracking(0, 0)

print(min_workload)
import random

# 사용자가 총 몇번 골랐는지 세는 변수
choice_count = 0
# [10][10] 공간을 담을 배열 선언
arr = []
# 총 몇회 시행할건지
max_count = 30

# 10x10 배열 arr에 0값으로 초기화
for i in range(10):
    arr.append([])
    for j in range(10):
        arr[i].append(0)


# 범위 안에 있는 배열만 찾아서 1씩 더하는 함수
def check_Range(row, col) :
# arr[i][j] = arr[i-1][j-1] ~ arr[i+1][j+1]
    for i in range(row-1, row+2) :
        for j in range(col-1, col+2) :
            if(i > 9 or i < 0 or j > 9 or j < 0) :
                pass
            else :
                arr[i][j] += 1
                # 1을 더했을 때 숫자가 9를 넘어가면 0으로 초기화
                if arr[i][j] > 9 :
                    arr[i][j] = 0
    print_score_table()
    
# 범위 내 배열 중에 9가 있으면 +1점 시키는 함수
def check_score() :
    score = 0
    for i in range(len(arr)) :
        for j in range(len(arr[i])) :
            if arr[i][j] == 9 :
                score += 1
    return score

# 현재 점수 배열 출력하는 함수
def print_score_table() :
    for i in arr :
        print(i)
    print()

# [10][10]배열의 숫자 위치를 시각적으로 표시하는 함수
def print_table() :
    for i in range(100) :
        print("|%4d" %(i+1), end=" ")
        if ((i+1) % 10 == 0) :
            print()

print("\n총 %d회 진행" %max_count)
while True :
    if (choice_count > max_count - 1) :
        print("--------------------게임 종료--------------------")
        total = check_score()
        print("총 점수 %d점" %total)
        break
    print_table()
    
    print("\n현재 카운트 횟수 : %d회/%d회" %(choice_count, max_count))
    choice_num = int(input("화면 속 번호 중 하나를 골라 주세요(1~100 종료:-999) : "))
    if (choice_num == -999) :
        print("--------------------게임 종료--------------------")
        break
    # 선택한 숫자가 범위를 벗어났을 때
    elif (choice_num > 100 or choice_num < 1) : 
        print("정해진 범위를 벗어났습니다. 다시 골라 주세요.\n")
    else:
        choice_count += 1
        #선택한 숫자를 배열 형식에 맞게 변환
        row = (choice_num - 1) // 10
        col = (choice_num - 1) % 10

        # 배열 범위 확인 후 1을 더하는 함수 호출
        check_Range(row, col)

        # 3회마다 랜덤 좌표 하나 더 증가
        if choice_count % 3 == 0:
            for i in range(2) :
                rand_num = random.randint(1, 100)
                rand_row = (rand_num - 1) // 10
                rand_col = (rand_num - 1) % 10
                print(f"[보너스] 랜덤 좌표 {rand_num} 에 +1 적용!")
                check_Range(rand_row, rand_col)


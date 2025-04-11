# 시계방향 회전
def rotate_clockwise(key: list[list[int]]):
    row_nums = len(key)
    column_nums = len(key[0])

    new = [[0] * column_nums for _ in range(row_nums)]

    # 그려보고 얻은 공식..(i, j)의 좌표는 (j, row_nums - 1 - i)의 위치로 이동함
    for i in range(row_nums):
        for j in range(column_nums):
            new[j][row_nums - 1 - i] = key[i][j]

    return new


# 자물쇠 해제 유무 확인
def is_unlocked(key: list[list[int]], locker: list[list[int]], x: int, y: int):
    n = len(locker)
    m = len(key)


    # 자물쇠 복제
    temp = [row[:] for row in locker]

    for i in range(m):
        for j in range(m):
            # Offset 활용 실제 좌표 변환
            new_x = i + x
            new_y = j + y

            # X, Y가 자물쇠 범위를 넘지 않는 곳에만 적용(index 초과 방지)
            if n > new_x >= 0 and n > new_y >= 0:
                temp[new_x][new_y] += key[i][j]
    
    # 자물쇠 모든 부분이 1이 되었는지 확인
    for row in temp:
        for column in row:
            if column != 1:
                return False
    
    return True



def solution(key: list[list[int]], locker: list[list[int]]):
    n = len(locker)
    m = len(key)
    
    # 360도 회전
    for _ in range(4):
        key = rotate_clockwise(key)
    
        for x in range(-m+1, n):
            for y in range(-m+1, n):
                # 열렸으면 리턴
                if is_unlocked(key, locker, x, y):
                    return True

    return False



print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
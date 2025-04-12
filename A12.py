def can_operate(frames: list[list[int]]):
    for x, y, material in frames:
        if material == 0:
            # 기둥이 위치할 수 있는 조건 OR로 확인

            # 1. 바닥 위
            # 2. 다른 기둥 위
            # 3. 보의 끝부분 위(보의 시작점 or 보의 시작점에 x + 1)
            if y == 0 \
                or [x, y - 1, 0] in frames \
                or [x, y, 1] in frames \
                or [x - 1, y, 1] in frames:
                continue
            
            return False
        else:
            # 보가 위치할 수 있는 조건 OR로 확인

            # 1. 현재 좌표의 기둥 (x, y - 1, 0)
            # 2. 우측 기둥 (현재 좌표 x + 1의 기둥) => (x + 1, y - 1, 0)
            # 3. 좌측의 보와 연결(현재 좌표 x - 1의 보) & 우측의 보와 연결(현재 좌표 x + 1의 보)
            if [x, y - 1, 0] in frames \
                or [x + 1, y - 1, 0] in frames \
                or ([x - 1, y, 1] in frames and [x + 1, y, 1] in frames):
                continue

            return False
            

    return True

def solution(n: int, build_frame: list[list[int]]):
    result = []

    for frame in build_frame:
        # x, y, 기둥/보, 삭제/설치
        x, y, material, operator = frame

        if operator == 0:
            # 삭제 후 불가시 원복
            result.remove([x, y, material])

            if not can_operate(result):
                result.append([x, y, material])
        if operator == 1:
            # 구조물 설치 후 불가시 원복
            result.append([x, y, material])

            if not can_operate(result):
                result.remove([x, y, material])

    return sorted(result)

# build_frame = [
#     [1, 0, 0, 1],
#     [1, 1, 1, 1],
#     [2, 1, 0, 1],
#     [2, 2, 1, 1],
#     [5, 0, 0, 1],
#     [5, 1, 0, 1],
#     [4, 2, 1, 1],
#     [3, 2, 1, 1]
# ]

build_frame = [
    [0, 0, 0, 1],
    [2, 0, 0, 1],
    [4, 0, 0, 1],
    [0, 1, 1, 1],
    [1, 1, 1, 1],
    [2, 1, 1, 1],
    [3, 1, 1, 1],
    [2, 0, 0, 0],
    [1, 1, 1, 0],
    [2, 2, 0, 1]
]

print(solution(5, build_frame))
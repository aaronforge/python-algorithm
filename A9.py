s = input()

answer = len(s)

for step in range(1, len(s) // 2 + 1):
    # 현재 스탭에서 압축된 결과 문자열
    compressed = ""

    # 이전 문자열 패턴 알파벳
    prev = s[0:step]
    
    # 동일 문자열 반복 횟수
    count = 1

    for j in range(step, len(s), step):
        if prev == s[j:j + step]:
            # 이전 문자열과 현재 순서 문자열 일치
            # 반복 수 더하기
            count += 1
        else:
            # 이전 문자열과 현재 순서 문자열 다름
            # 직전까지 압축 가능한 문자열 패턴 압축해서 덧붙여주기(카운트 1 이하면 그냥 문자 그대로)
            compressed += str(count) + prev if count > 1 else prev

            # 비교 문자열 현재 문자열로 변경
            prev = s[j:j+step]

            # 반복수 초기화
            count = 1
    
    # 남는 문자열 패턴 압축해서 덧붙여주기
    compressed += str(count) + prev if count > 1 else prev
    
    answer = min(answer, len(compressed))

print(answer)
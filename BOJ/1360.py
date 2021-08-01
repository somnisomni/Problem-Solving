# undo 부분 접근이 계속 잘못되어 타 블로그 글 참고함 : https://baby-ohgu.tistory.com/36

import sys
input = sys.stdin.readline

def process(N):
    buffer = ""
    timeline = []

    for _ in range(N):
        command, arg, sec = input().split()
        sec = int(sec)

        if command == "type":
            # 문자열 버퍼에 문자 추가
            buffer += arg
            timeline.append((sec, buffer))
        elif command == "undo":
            arg = int(arg)
            processed = False

            for i in range(len(timeline) - 1, -1, -1):
                # 현재 타임라인 아이템의 초가 되돌리기 범위 안인 경우 스킵
                if timeline[i][0] >= sec - arg:
                    continue
                # 범위에서 벗어난 경우 처리
                processed = True
                buffer = timeline[i][1]
                timeline.append((sec, buffer))
                break
            
            # 타임라인 역탐색을 완료해도 처리가 되지 않은 경우 문자열이 비어있는걸로 간주
            if not processed:
                buffer = ""
                timeline.append((sec, buffer))
    
    # 타임라인의 마지막 항목의 문자열 리턴
    return timeline[-1][1]

print(process(int(input())))
# AI 활용 자유 주제 파이썬 미니 프로젝트
# 이름 또는 학번: 
# 프로젝트 주제: 

#코드
import random
import time

def play_game():
    print("=== 알파벳 일치 게임 (1인 1알파벳 버전) ===")
    print("화면에 뜨는 랜덤 소문자 2개를 확인하세요.")
    print("▶ 플레이어 1은 '첫 번째' 알파벳을 입력합니다.")
    print("▶ 플레이어 2는 '두 번째' 알파벳을 입력합니다.")
    print("대문자나 공백을 입력하면 오답 처리되며 즉시 게임 오버!")
    print("-" * 50)

    score = 0
    limit_time = 5.0
    round_num = 1

    # 라운드 기록을 저장할 2차원 리스트
    game_records = []

    while True: # 게임 오버 전까지 무한 반복
        # 소문자 a(97) ~ z(122) 중에서 랜덤하게 2개 생성
        target1 = chr(random.randint(97, 122))
        target2 = chr(random.randint(97, 122))
        targets_str = f"{target1}, {target2}" # 기록용 문자열

        print(f"\n★ [라운드 {round_num}] 제시된 알파벳: {target1} , {target2} ★")

        # 플레이어 1은 첫 번째 알파벳(target1) 입력
        start_time1 = time.time()
        p1_input = input(f"플레이어 1 입력 (목표 '{target1}'): ")
        end_time1 = time.time()

        # 플레이어 2는 두 번째 알파벳(target2) 입력
        start_time2 = time.time()
        p2_input = input(f"플레이어 2 입력 (목표 '{target2}'): ")
        end_time2 = time.time()

        p1_duration = end_time1 - start_time1
        p2_duration = end_time2 - start_time2

        # 1. 제한시간 초과 검사
        if p1_duration > limit_time:
            print(f"\n[게임 오버] 플레이어 1 시간 초과! ({p1_duration:.2f}초)")
            game_records.append(
                [round_num, targets_str, p1_input, p2_input, "TIME OVER (P1)"]
            )
            break
        if p2_duration > limit_time:
            print(f"\n[게임 오버] 플레이어 2 시간 초과! ({p2_duration:.2f}초)")
            game_records.append(
                [round_num, targets_str, p1_input, p2_input, "TIME OVER (P2)"]
            )
            break

        # 2. 정답 및 일치 여부 검사 (각자 자신의 목표 알파벳과 정확히 일치해야 함)
        if p1_input == target1 and p2_input == target2:
            score += 1
            print(f"▶ 성공! 현재 점수: {score}점")
            game_records.append(
                [round_num, targets_str, p1_input, p2_input, "SUCCESS"]
            )
            round_num += 1
        else:
            print("\n[게임 오버] 알파벳을 잘못 입력했습니다!")
            game_records.append(
                [round_num, targets_str, p1_input, p2_input, "FAIL"]
            )
            break

    # 게임 종료 후 전체 기록(2차원 리스트) 출력
    print("\n" + "=" * 17 + " 게임 기록 " + "=" * 17)
    print("[라운드] |  [정답]  | [P1 입력] | [P2 입력] | [결과]")
    print("-" * 47)
    for record in game_records:
        print(
            f"   {record[0]:<2}    |   {record[1]}  |     {record[2]:<2}    |     {record[3]:<2}    | {record[4]}"
        )
    print("=" * 47)
    print(f"최종 점수: {score}점")


if __name__ == "__main__":
    play_game()
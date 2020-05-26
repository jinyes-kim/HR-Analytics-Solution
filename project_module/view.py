import datetime


def clear():
    for _ in range(100):
        print()


def load():
    print("┌────────────────────────────────────────┐ ")
    print("│           Data Loading...              │ ")
    print("└────────────────────────────────────────┘ ")


def start():
    print("┌────────────────────────────────────────┐ ")
    print("│           Management System            │ ")
    print("└────────────────────────────────────────┘ ")


def login_fail():
    print("┌────────────────────────────────────────┐ ")
    print("│ △ ID가 존재하지 않거나, PW가 다릅니다. 　│ ")
    print("└────────────────────────────────────────┘ ")
    print("\n 다시 시도 하시려면 아무 키나 입력해주세요.  ")


def warning():
    print("┌────────────────────────────────────────┐ ")
    print("│     △ 실행할 수 없는 명령어입니다.    │ ")         # 프롬프트 창에서 이 라인이 뷰 안 깨짐 참고용
    print("└────────────────────────────────────────┘ ")


def login_success(id):
    print(" ┌──── ")
    print("\t{}님 환영합니다.\n\t접속 시각: {}".format(id, datetime.datetime.now().strftime('%Y-%m-%d %H:%M')))
    print(" ───────────────────────────────── ")
    print("\n\n")


def time_now():
    print("                                     {}".format(datetime.datetime.now().strftime('%H:%M')))


def menu_main(admin):
    if admin == 1:
        print("┌────────────────────────────────────────┐ ")
        print("│    Menu                                │ ")
        print("└────────────────────────────────────────┘ ")
        print("┌─ ")
        print("│   (1) 조직도")
        print("│   (2) 직원 조회")
        print("│   (3) 직원 통계")
        print("│   (4) 이탈 예측")
        print("│   (0) 종료")
        print("└───────────────────────────────────────── ")
    else:
        print("┌────────────────────────────────────────┐ ")
        print("│    Menu                                │ ")
        print("└────────────────────────────────────────┘ ")
        print("┌─ ")
        print("│   (1) 조직도")
        print("│   (2) 직원 조회")
        print("│   (0) 종료")
        print("└───────────────────────────────────────── ")


def menu_organize():
    print("┌────────────────────────────────────────┐ ")
    print("│    Organization Chart                  │ ")
    print("└────────────────────────────────────────┘ ")
    print("┌─ ")
    print("│   (1) Human Resources")
    print("│   (2) Research & Development")
    print("│   (3) Sales")
    print("│   (0) 뒤로가기")
    print("└───────────────────────────────────────── ")


def menu_search_employee():
    print("┌────────────────────────────────────────┐ ")
    print("│   Employee Search                      │ ")
    print("└────────────────────────────────────────┘ ")
    print("┌─ ")
    print("│   (1) 전체 조회")
    print("│   (2) 키워드 조회")
    print("│   (0) 뒤로가기")
    print("└───────────────────────────────────────── ")


def menu_statistic():
    print("┌────────────────────────────────────────┐ ")
    print("│    Statistics                          │")
    print("└────────────────────────────────────────┘ ")
    print("┌─ ")
    print("│   (1) 전체 요약 정보")
    print("│   (2) 나이")
    print("│   (3) 성별")
    print("│   (4) 퇴직")
    print("│   (5) 부서")
    print("│   (6) 직무")
    print("│   (7) 혼인")
    print("│   (8) 급여")
    print("│   (9) 성과")
    print("│   (10) 야근")
    print("│   (11) 잡 레벨")
    print("│   (0) 뒤로가기")
    print("└───────────────────────────────────────── ")


def menu_management():
    print("┌────────────────────────────────────────┐ ")
    print("│    Personal Management                 │ ")
    print("└────────────────────────────────────────┘ ")
    print("┌─ ")
    print("│   (1) 임시 화면")
    print("│   (2) 임시화면")
    print("│   (2) 임시화면")
    print("│   (2) 임시화면")
    print("│   (2) 임시화면")
    print("│   (0) 뒤로가기")
    print("└───────────────────────────────────────── ")

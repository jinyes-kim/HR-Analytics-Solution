import datetime
from custom_module import login
from custom_module import load

# DB & user data load
login.view_load()
try:
    db = login.connect_db()

except Exception as err:
    print("ERROR: {}".format(err))

try:
    data = load.load_file()
except:
    print("ERROR: {}".format(err))

login.view_init()
buffer = input()

# main
ban = 0
while True:
    success = False
    login.clear_screen()
    login.view_start()
    id_input = input('ID: ')
    pw_input = input('PW: ')
    try:
        if login.login(db, id_input, pw_input):
            user = login.User(id_input, db[id_input][2])
            login.clear_screen()
            login.view_login(id_input)
            print("\n{}님 환영합니다.\n접속 시각: {}".format(user.id, datetime.datetime.now()))
            success = True
        else:
            raise KeyError
    except:
        print("\nID가 존재하지 않거나 PASSWORD가 다릅니다.")
        print("다시 로그인 하시려면 ENTER를 눌러주세요")
        buffer = input()
        login.clear_screen()
        ban += 1
        if ban == 3:
            print("잘못된 접근으로 인한 IP 차단")
            break

    if success:
        while True:
            print("======Menu=====\n(1) 조회\n(2) 조직도\n(3) 인사 관리\n(0) 종료")
            try:
                n = int(input("\n=> "))
            except:
                print("실행할 수 없는 명령어입니다.")
            if n == 0:
                break
            elif n == 1:
                login.clear_screen()
                print("======Menu=====\n(1) 전체 출력\n(2) 키워드 출력\n(0) 뒤로가기")
                while True:
                    n = int(input("\n=>"))
                    if n == 1:
                        for a in data:
                            a.print_HR()
                        break
                    elif n == 0:
                        break
                    else:
                        print("잘못된 명령어입니다.")



# -*- coding: utf-8 -*-

import time
import user
import employee
from custom_module import search
from custom_module import statistic
from custom_module import view
from custom_module import login
from custom_module import load


# DB & data load
try:
    db = login.connect_db()
except Exception as err:
    print("ERROR: {}".format(err))

try:
    data = load.load_file()
except Exception as err:
    print("ERROR: {}".format(err))


# login effect
view.load()
time.sleep(1)
view.clear()
view.init()
buffer = input()

# main
ban = 0
while True:
    success = False
    view.clear()
    view.start()

    # login
    id_input = input('ID: ')
    pw_input = input('PW: ')
    if login.login(db, id_input, pw_input):
        success = True
    else:
        view.login_fail()
        buffer = input()
        view.clear()
        ban += 1
        if ban == 3:
            print("잘못된 접근으로 인한 IP 차단")
            break

    # start menu
    if success:
        identity = user.User(id_input, db[id_input][2]) # 유저 객체로 권한 부여
        view.clear()
        view.login_success(id_input)
        while True:
            identity.print_identity()
            view.menu_main(identity.power)
            try:
                n = int(input("\n=> "))
            except:
                print("잘못된 명령어입니다.")
            if n == 0:
                break

            # 조직도
            elif n == 1:
                view.clear()
                while True:
                    view.menu_organize()
                    try:
                        n = int(input("\n=> "))
                    except:
                        print("잘못된 명령어입니다.")
                        continue
                    if n == 0:
                        view.clear()
                        break
                    elif n == 1:
                        print("Department: Human Resources")
                        for a in data:
                            if search.search_organize(a, 'Human Resources'):
                                a.print_HR(identity.power)
                    elif n == 2:
                        print("Department: Research & Development")
                        for a in data:
                            if search.search_organize(a, 'Research & Development'):
                                a.print_HR(identity.power)
                    elif n == 3:
                        print("Department: Sales")
                        for a in data:
                            if search.search_organize(a, 'Sales'):
                                a.print_HR(identity.power)
                    else:
                        print("잘못된 명령어입니다.")
                        continue

            # 직원 조회
            elif n == 2:
                view.clear()
                while True:
                    view.menu_search_employee()
                    try:
                        print("메뉴를 입력하세요.")
                        n = int(input("\n=> "))
                    except:
                        print("잘못된 명령어입니다.")
                        continue

                    if n == 0:
                        break
                    elif n == 1:
                        employee.print_column(identity.power)
                        for a in data:
                            a.print_HR(identity.power)
                    elif n == 2:
                        print("검색할 키워드를 입력해주세요.")
                        kwd = input("\n=>")
                        for a in data:
                            if search.search_keyword(a, kwd):
                                a.print_HR(identity.power)
                    else:
                        print("잘못된 명령어입니다.")
                        continue

            # 직원 통계
            elif n == 3:
                while True:
                    if identity.power == 1:
                        view.clear()
                        view.menu_statistic()
                        try:
                            n = int(input("\n=> "))
                        except:
                            print("잘못된 명령어입니다.")
                        if n == 0:
                            break
                        elif n == 1:
                            print("전체 요약 통계")
                            statistic.statistic(data)
                            pass
                        else:
                            print("잘못된 명령어입니다.")
                    else:
                        print("잘못된 명령어입니다.")
                        break

            # 인사 관리
            elif n == 4:
                while True:
                    if identity.power == 1:
                        view.clear()
                        view.menu_management()
                        try:
                            n = int(input("\n=> "))
                        except:
                            print("잘못된 명령어입니다.")
                        if n == 0:
                            break
                        elif n == 1:
                            pass
                        else:
                            print("잘못된 명령어입니다.")
                    else:
                        print("잘못된 명령어입니다.")
                        break

            else:
                print("잘못된 명령어입니다.")

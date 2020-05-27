import time
import user
import employee
from custom_module import search
from custom_module import statistic
from custom_module import view
from custom_module import login
from custom_module import load

"""
남은 일

summary 함수 레이 아웃 수정
이탈 위험 모델 적용
"""
# DB & data load
try:
    db = login.connect_db()
except Exception as err:
    print("ERROR: {}".format(err))

try:
    data = load.load_file()
    att_data = load.load_file(att=True)
    not_att_data = load.load_file(not_att=True)
except Exception as err:
    print("ERROR: {}".format(err))

# login effect
view.load()
time.sleep(1)
view.clear()

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
            view.time_now()
            try:
                n = int(input("\n=> "))
            except:
                view.clear()
                view.warning()
                continue
            if n == 0:
                break

            # 조직도
            elif n == 1:
                view.clear()
                while True:
                    view.menu_organize()
                    view.time_now()
                    try:
                        n = int(input("\n=> "))
                    except:
                        view.clear()
                        view.warning()
                        continue
                    if n == 0:
                        view.clear()
                        break
                    elif n == 1:
                        print("Department: Human Resources")
                        employee.print_column(identity.power)
                        for a in data:
                            if search.search_organize(a, 'Human Resources'):
                                a.print_HR(identity.power)
                    elif n == 2:
                        print("Department: Research & Development")
                        employee.print_column(identity.power)
                        for a in data:
                            if search.search_organize(a, 'Research & Development'):
                                a.print_HR(identity.power)
                    elif n == 3:
                        print("Department: Sales")
                        employee.print_column(identity.power)
                        for a in data:
                            if search.search_organize(a, 'Sales'):
                                a.print_HR(identity.power)
                    else:
                        view.clear()
                        view.warning()
                        continue

            # 직원 조회
            elif n == 2:
                view.clear()
                while True:
                    view.menu_search_employee()
                    view.time_now()
                    try:
                        print("메뉴를 입력하세요.")
                        n = int(input("\n=> "))
                    except:
                        view.clear()
                        view.warning()
                        continue

                    if n == 0:
                        view.clear()
                        break
                    elif n == 1:
                        employee.print_column(identity.power)
                        for a in data:
                            a.print_HR(identity.power)
                    elif n == 2:
                        print("검색할 키워드를 입력해주세요.")
                        kwd = input("\n=>")
                        kwd = kwd.split(" ")
                        employee.print_column(identity.power)
                        for a in data:
                            if search.search_multi(a, kwd):
                                a.print_HR(identity.power)
                    else:
                        view.clear()
                        view.warning()
                        continue

            # 직원 통계
            elif n == 3:
                while True:
                    tmp = True
                    if identity.power == 1:
                        #view.clear()    # 메뉴 유추 못하게 안에서 돌게 한다.
                        view.menu_statistic()
                        view.time_now()
                        try:
                            n = int(input("\n=> "))
                        except:
                            view.clear()
                            view.warning()
                            continue
                        if n == 0:
                            view.clear()
                            break
                        elif n == 1:
                            print("전체 요약 통계")
                            df = statistic.summary_data(data)
                        elif n == 2:
                            print("평균 나이")
                            statistic.numeric_graph(data, 'Age')
                            view.clear()
                        elif n == 3:
                            print("성별 비율")
                            statistic.cate_graph(data, 'Gender')
                            view.clear()
                        elif n == 4:
                            print("이탈 비율")
                            statistic.cate_graph(data, 'Attrition')
                            view.clear()
                        elif n == 5:
                            print("부서 비율")
                            statistic.cate_graph(data, 'Department')
                            view.clear()
                        elif n == 6:
                            print("직무 비율")
                            statistic.cate_graph(data, 'JobRole')
                            view.clear()
                        elif n == 7:
                            print("결혼 비율")
                            statistic.cate_graph(data, 'MaritalStatus')
                            view.clear()
                        elif n == 8:
                            print("평균 급여")
                            statistic.numeric_graph(data, 'MonthlyIncome')
                            view.clear()
                        elif n == 9:
                            print("평균 성과")
                            statistic.numeric_graph(data, 'MonthlyRate')
                            view.clear()
                        elif n == 10:
                            print("야근 비율")
                            statistic.cate_graph(data, 'OverTime')
                            view.clear()
                        elif n == 11:
                            print("잡 레벨")
                            statistic.cate_graph(data, 'JobLevel')
                            view.clear()
                        else:
                            view.clear()
                            view.warning()
                            continue
                    else:
                        view.clear()
                        break

            # 비교 분석
            elif n == 4:
                while True:
                    if identity.power == 1:
                        view.clear()
                        view.menu_compare()
                        view.time_now()
                        try:
                            n = int(input("\n=> "))
                        except:
                            view.clear()
                            view.warning()
                            continue
                        if n == 0:
                            view.clear()
                            break
                        elif n == 1:
                            print("[이탈 직원]")
                            statistic.summary_data(att_data)
                            print("[재직 직원]")
                            statistic.summary_data(not_att_data)

                        elif n == 2:
                            statistic.compare_graph(data)
                            view.clear()
                        else:
                            view.clear()
                            view.warning()
                    else:
                        view.clear()
                        view.warning()
                        break
            elif n == 5:
                while True:
                    if identity.power == 1:
                        view.clear()
                        view.menu_predict()
                        view.time_now()
                        try:
                            n = int(input("\n=> "))
                        except:
                            view.clear()
                            view.warning()
                            continue
                        if n == 0:
                            view.clear()
                            break
                        elif n == 1:
                            pass
                        else:
                            view.clear()
                            view.warning()
                    else:
                        view.clear()
                        view.warning()
                        break
            else:
                view.clear()
                view.warning()
                continue

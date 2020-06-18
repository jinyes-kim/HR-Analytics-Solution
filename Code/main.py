import time
import user
import employee
from custom_module import *
import matplotlib.pyplot as plt

# DB & data load
try:
    db = login.connect_db()
except Exception as err:
    print("ERROR: {}".format(err))

try:
    data = load.load_file()
    att_data = load.load_file(att=True)
    not_att_data = load.load_file(not_att=True)
    data_label = [att_data, not_att_data]
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
                del identity
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
                        dummy = True
                        for a in data:
                            if search.search_multi(a, kwd):
                                a.print_HR(identity.power)
                                dummy = False
                        if dummy:
                            view.data_not_exist()
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
                            print("[전체 데이터 - 기초 통계 분석] ")
                            df = statistic.summary_data(data)
                            view.buffer_dummy()
                            buffer = input()
                        elif n == 2:
                            print("평균 나이")
                            statistic.numeric_graph(data, 'Age')
                            plt.show()
                            view.clear()
                        elif n == 3:
                            print("성별 비율")
                            statistic.cate_graph(data, 'Gender')
                            plt.show()
                            view.clear()
                        elif n == 4:
                            print("이탈 비율")
                            statistic.cate_graph(data, 'Attrition')
                            plt.show()
                            view.clear()
                        elif n == 5:
                            print("부서 비율")
                            statistic.cate_graph(data, 'Department')
                            plt.show()
                            view.clear()
                        elif n == 6:
                            print("직무 비율")
                            statistic.cate_graph(data, 'JobRole')
                            plt.show()
                            view.clear()
                        elif n == 7:
                            print("결혼 비율")
                            statistic.cate_graph(data, 'MaritalStatus')
                            plt.show()
                            view.clear()
                        elif n == 8:
                            print("평균 급여")
                            statistic.numeric_graph(data, 'MonthlyIncome')
                            plt.show()
                            view.clear()
                        elif n == 9:
                            print("평균 성과")
                            statistic.numeric_graph(data, 'MonthlyRate')
                            plt.show()
                            view.clear()
                        elif n == 10:
                            print("야근 비율")
                            statistic.cate_graph(data, 'OverTime')
                            plt.show()
                            view.clear()
                        elif n == 11:
                            print("잡 레벨")
                            statistic.cate_graph(data, 'JobLevel')
                            plt.show()
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
                            print("[퇴직 직원 - 기초 통계]")
                            statistic.summary_data(att_data)
                            print("[재직 직원 - 기초 통계]")
                            statistic.summary_data(not_att_data)
                            view.buffer_dummy()
                            buffer = input()
                        elif n == 2:
                            statistic.compare_graph(data)
                            view.clear()
                        elif n == 3:
                            print("평균 나이")
                            statistic.multi_graph('Age', data_label, cate=False)
                            plt.show()
                            view.clear()
                        elif n == 4:
                            print("성별 비율")
                            statistic.multi_graph('Gender', data_label)
                            plt.show()
                            view.clear()
                        elif n == 5:
                            print("이탈 비율")
                            statistic.multi_graph('Attrition', data_label)
                            plt.show()
                            view.clear()
                        elif n == 6:
                            print("부서 비율")
                            statistic.multi_graph('Department', data_label)
                            plt.show()
                            view.clear()
                        elif n == 7:
                            print("직무 비율")
                            statistic.multi_graph('JobRole', data_label)
                            plt.show()
                            view.clear()
                        elif n == 8:
                            print("결혼 비율")
                            statistic.multi_graph('MaritalStatus', data_label)
                            plt.show()
                            view.clear()
                        elif n == 9:
                            print("평균 급여")
                            statistic.multi_graph('MonthlyIncome', data_label, cate=False)
                            plt.show()
                            view.clear()
                        elif n == 10:
                            print("평균 성과")
                            statistic.multi_graph('MonthlyRate', data_label, cate=False)
                            plt.show()
                            view.clear()
                        elif n == 11:
                            print("야근 비율")
                            statistic.multi_graph('OverTime', data_label)
                            plt.show()
                            view.clear()
                        elif n == 12:
                            print("잡 레벨")
                            statistic.multi_graph('JobLevel', data_label)
                            plt.show()
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
                            employee.print_column(identity.power)
                            for a in not_att_data:
                                if statistic.predict_att(a):
                                    a.print_HR(identity.power)
                            view.buffer_dummy()
                            buffer = input()
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

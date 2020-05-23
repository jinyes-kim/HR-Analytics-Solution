# 인컴 대비 레이트가 높은 직원들을 일정 비율로 출력하기
# 이탈 직원들의 인컴과 레이트 비율을 계산하고 그 비율을 기준치로 삼아서
# 아직 이탈하지 않은 직원들 중에서 이탈 직원과 그 rate/ income 수치가 높으면
# 이탈 위험직군으로 분류하는 알고리즘


import matplotlib.pyplot as plt

"""
1. 각각 속성별 통계 - 남녀 비율, 이탈 비율, 평균 수입, 평균 성과
2. 부서별 통계 - 부서별 인원, 부서별 평균 임금, 부서별 평균 성과
3. 성과 상위 30 명 - 레이팅 줄 세우기
4. 이탈 위험 직원 -
"""


def dict_to_category(data_dict):
    res = []
    for a in data_dict:
        if a not in res:
            res.append(a)
    return res


def dict_to_list(data_dict):
    res = []
    for a in data_dict:
        res.append(data_dict[a])
    return res


def sum_dict(data_dict, data):
    if data in data_dict:
        data_dict[data] += 1
    else:
        data_dict[data] = 0


def statistic(data, part=False):
    # data is employee instance

    # Age, gender, Attrition, department, jobRole, married, income, rate
    sum_age = 0
    gender_dict = {}
    att_dict = {}
    depart_dict = {}
    role_dict = {}
    marry_dict = {}
    sum_income= 0
    sum_rate = 0

    if not part:
        for a in data:
            sum_age += int(a.age)
            sum_dict(gender_dict, a.gender)
            sum_dict(att_dict, a.attrition)
            sum_dict(depart_dict, a.department)
            sum_dict(role_dict, a.job_role)
            sum_dict(marry_dict, a.marital_status)
            sum_income += int(a.income)
            sum_rate += int(a.rate)


    else:
        # 부서별 통계
        pass

    sum_age /= len(data)
    sum_income /= len(data)
    sum_rate /= len(data)

    print("평균 나이: ", sum_age)
    print("성별 분포: ", gender_dict)
    print("이탈 비율: ", att_dict)
    print("부서 분포: ", depart_dict)
    print("직무 분포: ", role_dict)
    print("결혼 비율: ", marry_dict)
    print("평균 급여: ", sum_income)
    print("평균 성과: ", sum_rate)

    gender_data = dict_to_list(gender_dict)
    gender_category = dict_to_category(gender_dict)
    plt.pie(gender_data, labels=gender_category, autopct="%.1f%%")
    
    # 위 코드 기반으로 서브플롯 그려서 각 항몽에 대한 파이 파트 출력
    plt.show()


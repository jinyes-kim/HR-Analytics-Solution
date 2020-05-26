try:
    import pandas as pd
except ImportError as err:
    print("라이브러리를 설치해주세요. {}".format(err))

try:
    import matplotlib.pyplot as plt
except ImportError as err:
    print("라이브러리를 설치해주세요. {}".format(err))


def dict_to_category(data_dict):
    res = []
    for a in data_dict:
        if a not in res:
            res.append(a)
    return res


# 딕셔너리 키들의 분포 비율 계산
def cal_ratio(data_dict):
    ratio = []
    sum = 0
    for a in data_dict:
        sum += data_dict[a]
    for a in data_dict:
        ratio.append(data_dict[a] / sum)
    return ratio


def print_dict(data_dict):
    for a in data_dict:
        print("{}: {}".format(a, data_dict[a]))


# 데이터셋이 리스트 안에 객체로 존재하는 상태.
def make_df(data):
    tmp = []
    label = ['Age',	'Attrition', 'Department', 'EmployeeNumber', 'Gender', 'JobLevel', 'JobRole',
             'MaritalStatus', 'MonthlyIncome', 'MonthlyRate', 'OverTime']
    for a in data:
        tmp.append(a.total)
    df = pd.DataFrame(tmp, columns=label)
    return df


def list_to_dict(data_list):
    data_dict = {}
    for a in data_list:
        if a in data_dict:
            data_dict[a] += 1
        else:
            data_dict[a] = 0
    return data_dict


def cate_graph(data, kwd):
    df = make_df(data)
    tmp = df[kwd]
    data_dict = list_to_dict(tmp)
    print_dict(data_dict)
    col = dict_to_category(data_dict)
    plt.pie(cal_ratio(data_dict), labels=col, autopct="%.1f%%")
    plt.title(kwd)
    plt.show()


def numeric_graph(data, kwd):
    df = make_df(data)
    tmp = df[kwd]
    tmp = list(map(int, tmp))
    avg = sum(tmp) / len(tmp)
    print("평균 {}: {:.2f}".format(kwd, avg))

    binn = 0
    if kwd == 'Age':
        binn = 10
    else:
        binn = 100
    plt.hist(tmp, label=kwd, bins=binn, )
    plt.title(kwd)
    plt.tick_params(axis='both', which='both', direction='in', pad=8, top=True, right=True)
    plt.show()


def summary_data(data):
    # 출력 모양 이쁘게 변환, 평균 사분위수 계산
    df = make_df(data)
    for kwd in df.columns:
        if kwd == 'EmployeeNumber':
            continue
        if kwd == "Age" or kwd == 'MonthlyIncome' or kwd == 'MonthlyRate':
            tmp = df[kwd]
            tmp = list(map(int, tmp))
            avg = sum(tmp) / len(tmp)
            print("[요약: {}]".format(kwd))
            print("{}: {:.2f}\n\n".format(kwd, avg))
        else:
            tmp = df[kwd]
            data_dict = list_to_dict(tmp)
            print("[요약: {}]".format(kwd))
            print_dict(data_dict)
            print()

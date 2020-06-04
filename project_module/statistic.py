try:
    import numpy as np
except ImportError as err:
    print("라이브러리를 설치해주세요. {}".format(err))

try:
    import pandas as pd
except ImportError as err:
    print("라이브러리를 설치해주세요. {}".format(err))

try:
    import matplotlib.pyplot as plt
except ImportError as err:
    print("라이브러리를 설치해주세요. {}".format(err))

try:
    import seaborn as sns
    sns.set()
    colors = sns.color_palette("pastel")
except ImportError as err:
    print("라이브러리를 설치해주세요. {}".format(err))
    print("필수 라이브러리: scipy, statsmodels")


def dict_to_category(data_dict):
    res = []
    for a in data_dict:
        if a not in res:
            res.append(a)
    return res


def list_to_dict(data_list):
    data_dict = {}
    for a in data_list:
        if a in data_dict:
            data_dict[a] += 1
        else:
            data_dict[a] = 0
    return data_dict


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


def cate_graph(data, kwd):
    df = make_df(data)
    tmp = df[kwd]
    data_dict = list_to_dict(tmp)
    print_dict(data_dict)
    col = dict_to_category(data_dict)

    # pie chart
    plt.pie(cal_ratio(data_dict), labels=col, autopct="%.1f%%",
            startangle=90, pctdistance=0.85, colors=colors)
    plt.title(kwd)

    # draw circle
    centre_circle = plt.Circle((0, 0), 0.70, fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
    plt.tight_layout()


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
    sns.distplot(tmp, kde=True);
    plt.title(kwd)


def summary_data(data):
    pd.options.display.float_format = '{:.2f}'.format
    df = make_df(data)
    for kwd in df.columns:
        if kwd == 'EmployeeNumber':
            continue
        if kwd == "Age" or kwd == 'MonthlyIncome' or kwd == 'MonthlyRate':
            tmp = df[kwd]
            tmp = list(map(int, tmp))
            tmp = pd.Series(tmp)
            print("[{}]".format(kwd))
            print(tmp.describe(), end='\n\n')
        else:
            tmp = df[kwd]
            data_dict = list_to_dict(tmp)
            print("[{}]".format(kwd))
            print_dict(data_dict)
            print()


def compare_graph(data):
    df = make_df(data)
    compare_col = []
    for col in df.columns:
        if col == "EmployeeNumber" or col == "Attrition":
            continue
        else:
            compare_col.append(col)

    # 통계 에디터가 아니라서 해당 전처리가 필요하다.
    tmp = []
    for a in df["MonthlyIncome"]:
        tmp.append((int(a) / 1000) * 1000)
    df["MonthlyIncome"] = tmp

    tmp = []
    for a in df["MonthlyRate"]:
        tmp.append((int(a) / 1000) * 1000)
    df["MonthlyRate"] = tmp

    # density histogram
    plt.figure(figsize=(10, 10))
    for i, column in enumerate(compare_col, 1):
        if column == "EmployeeNumber" or column == "Attrition":
            continue
        plt.subplot(3, 3, i)
        df[df["Attrition"] == 'No'][column].hist(
            bins=20, color='green', label='Attrition = NO', alpha=0.5, density=True)
        df[df["Attrition"] == 'Yes'][column].hist(
            bins=20, color='red', label='Attrition = YES', alpha=0.5, density=True)
        plt.legend()
        plt.xlabel(column)
    plt.tight_layout()
    plt.show()


def multi_graph(kwd, data_label, cate=True):
    #data_label = [att_data, not_att_data]
    if cate:
        att_label = ['Attrition Yes', 'Attrition No']
        plt.subplot(1, 2, 1)
        cate_graph(data_label[0], kwd)
        plt.title(att_label[0] + ' - ' + kwd)
        plt.subplot(1, 2, 2)
        cate_graph(data_label[1], kwd)
        plt.title(att_label[1] + ' - ' + kwd)
    else:
        att_label = ['Attrition Yes', 'Attrition No']
        plt.subplot(1, 2, 1)
        numeric_graph(data_label[0], kwd)
        plt.title(att_label[0] + ' - ' + kwd)
        plt.subplot(1, 2, 2)
        numeric_graph(data_label[1], kwd)
        plt.title(att_label[1] + ' - ' + kwd)


def predict_att(employee):
    if employee.overTime == 'yes' and employee.marital_status == 'Single' and employee.job_level == '1':
        return True
    return False

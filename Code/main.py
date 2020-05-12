from project_module import load_data

data = []
print('Input File Name\n')
file_name = input("=> ")
with open('./data/'+file_name, 'r') as file:
    for idx, line in enumerate(file):
        if idx == 0:
            continue
        data.append(load_data.HR(line))

while True:
    order = int(input('명령어 입력 => '))
    if order == 0:
        break
    else:
        print('ID\t\tAge\t\tGender\t\tAttrition\t\tDepartment\t\tDistanceFromHome\t\tMajor\t\t\t\tJob Role\t\tSatisfaction'
              '\t\tMarital Status\t\tIncome\t\tRate')
        for a in data:
            a.print_HR()

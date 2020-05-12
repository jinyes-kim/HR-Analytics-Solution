from project_module.load_data import HR
from project_module.load_data import print_column

data = []
print('Input File Name\n')
file_name = input("=> ")
with open('./data/'+file_name, 'r') as file:
    for idx, line in enumerate(file):
        if idx == 0:
            continue
        data.append(HR(line))

while True:
    order = int(input('명령어 입력 => '))
    if order == 0:
        break
    else:
        print_column()
        for a in data:
            a.print_HR()

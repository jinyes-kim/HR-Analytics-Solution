import employee


def load_file(att=False, not_att=False):
    data = []
    with open('./data/data.csv', 'r') as file:
        for idx, line in enumerate(file):
            tmp = line.split(',')
            if idx == 0:
                continue
            if att:
                if tmp[1] == 'Yes':
                    data.append(employee.Employee(line))
            elif not_att:
                if tmp[1] == 'No':
                    data.append(employee.Employee(line))
            else:
                data.append(employee.Employee(line))
    return data

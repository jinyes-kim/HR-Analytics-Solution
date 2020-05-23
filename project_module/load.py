import employee


def load_file():
    data = []
    with open('./data/data.csv', 'r', encoding='UTF-8') as file:
        for idx, line in enumerate(file):
            if idx == 0:
                continue
            data.append(employee.Employee(line))
    return data

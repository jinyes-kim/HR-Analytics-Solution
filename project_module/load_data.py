class HR:
    def __init__(self, line):
        # Age	Attrition	Department	DistanceFromHome    EducationField
        # EmployeeNumber	Gender	JobRole	JobSatisfaction	MaritalStatus	MonthlyIncome	MonthlyRate
        tmp = line.split(',')
        self.age = tmp[0]
        self.attrition = tmp[1]
        self.department = tmp[2]
        self.distance_home = tmp[3]
        self.major = tmp[4]
        self.id = tmp[5]
        self.gender = tmp[6]
        self.job_role = tmp[7]
        self.satisfaction = tmp[8]
        self.marital_status = tmp[9]
        self.income = tmp[10]
        self.rate = tmp[11]

    def print_HR(self):
        print('[{:>4}]\t{:>2}\t{:>10}\t{:>10}\t{:>20}\t{:>5}\t\t\t{:>20}\t{:>20}\t{:>3}\t\t\t{:>10}\t\t{:>10}\t\t{:>10}'.
              format(self.id, self.age, self.gender, self.attrition, self.department, self.distance_home,
                     self.major, self.job_role, self.satisfaction, self.marital_status,
                     self.income, self.rate))


def print_column():
    print('ID\t\tAge\t\tGender\t\tAttrition\t\tDepartment\t\tDistanceFromHome\t\tMajor\t\t\t\tJob Role\t\tSatisfaction'
          '\t\tMarital Status\t\tIncome\t\tRate')

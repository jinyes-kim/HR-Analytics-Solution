class Employee:
    def __init__(self, line):
        #  Age	Attrition	Department	EmployeeNumber	Gender	JobLevel
        #  JobRole	MaritalStatus	MonthlyIncome	MonthlyRate	 OverTime

        self.total = line.split(',')
        self.age = self.total[0]
        self.attrition = self.total[1]
        self.department = self.total[2]
        self.id = self.total[3]
        self.gender = self.total[4]
        self.job_level = self.total[5]
        self.job_role = self.total[6]
        self.marital_status = self.total[7]
        self.income = self.total[8]
        self.rate = self.total[9]
        self.overTime = self.total[10]
        self.overTime = ''.join(ch.lower() for ch in self.total[10] if ch.isalnum())

    def print_HR(self, admin):
        if admin == 1:
            print(
                '[{:>4}]\t{:>6}\t{:>2}\t{:>2}\t{:>6}\t{:>20}\t{:>20}\t{:>10}\t{:>8}\t{:>8}\t{:>6}'.
                format(self.id, self.attrition, self.age, self.job_level, self.gender,  self.department, self.job_role,
                       self.marital_status, self.income, self.rate, self.overTime))
        else:
            print(
                '[{:>4}]\t{:>2}\t{:>10}\t{:>20}\t{:>10}'.
                format(self.id, self.age, self.gender, self.department, self.job_role))


def print_column(admin):
    if admin == 1:
        print('ID   Attrition   Age\tjobLevel  Gender\tDepartment\t\tJob Role\tMarital Status\tIncome\t\tRate\t\toverTime')
    else:
        print('ID\tAge\t\tGender\t\tDepartment\tJob Role')

# -*- coding: utf-8 -*-
class Employee:
    def __init__(self, line):
        # Age	Attrition	Department	DistanceFromHome X    EducationField X
        # EmployeeNumber	Gender	JobRole	JobSatisfaction	 MaritalStatus	 MonthlyIncome	 MonthlyRate


        # 받을 것만 받을 건지 정리 필요함
        self.total = line.split(',')
        self.age = self.total[0]
        self.attrition = self.total[1]
        self.department = self.total[2]
        self.distance_home = self.total[3]
        self.major = self.total[4]
        self.id = self.total[5]
        self.gender = self.total[6]
        self.job_role = self.total[7]
        self.satisfaction = self.total[8]
        self.marital_status = self.total[9]
        self.income = self.total[10]
        self.rate = self.total[11]

    def print_HR(self, admin):
        if admin == 1:
            print(
                '[{:>4}]\t{:>2}\t{:>10}\t{:>10}\t{:>20}\t{:>20}\t{:>10}\t{:>10}\t{:>10}'.
                format(self.id, self.age, self.gender, self.attrition, self.department, self.job_role,
                       self.marital_status, self.income, self.rate))
        else:
            print(
                '[{:>4}]\t{:>2}\t{:>10}\t{:>20}\t{:>10}'.
                format(self.id, self.age, self.gender, self.department, self.job_role))


def print_column(admin):
    if admin == 1:
        print('ID\t\tAge\t\tGender\t\tAttrition\t\tDepartment\t\t\tJob Role\t\tMarital Status\t\tIncome\tRate')
    else:
        print('ID\t\tAge\t\tGender\t\tDepartment\t\t\tJob Role')

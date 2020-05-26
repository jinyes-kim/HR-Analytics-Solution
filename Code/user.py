class User:
    def __init__(self, id, power):
        self.id = id
        self.power = power

    def print_identity(self):
        level = ['일반 사용자', '관리자']
        print(" 성명: {}\t권한: {}".format(self.id, level[self.power]))

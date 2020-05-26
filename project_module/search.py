# 추가 기능 - 다중 검색 기능

# 해당하는 부서에 해당하면 필터링
def search_organize(employee, keyword):
    if keyword == employee.department:
        return True
    else:
        return False


# 키워드에 해당하는 직원 필터링
def search_keyword(employee, keyword):
    temp = employee.total
    if keyword.isalpha():
        for kwd in temp:
            kwd = kwd.lower()
            if kwd == 'male' or kwd == 'female':
                if kwd == keyword:
                    return True
            elif keyword in kwd:
                return True

    else:
        keyword = int(keyword)

        if keyword < 100:
            if keyword-10 < int(employee.age) < keyword+10:
                return True
        else:
            if keyword - 500 < int(employee.income) < keyword + 500:
                return True
            elif keyword - 1000 < int(employee.rate) < keyword + 1000:
                return True
    return False


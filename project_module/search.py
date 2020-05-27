def search_organize(employee, keyword):
    if keyword == employee.department:
        return True
    else:
        return False


def search_keyword(employee, keyword):
    temp = employee.total
    keyword = keyword.lower()
    if keyword.isalpha():
        for kwd in temp:
            kwd = kwd.lower()
            if kwd == 'male' or kwd == 'female':
                if kwd == keyword:
                    return True
            elif keyword == 'yes' or keyword == 'no':
                if kwd == keyword:
                    return True
            elif keyword in kwd:
                return True
    else:
        keyword = int(keyword)

        if keyword < 90:
            if int(str(keyword)[0]+'0') < int(employee.age) < keyword+9:
                return True
        else:
            if keyword - 500 < int(employee.income) < keyword + 500:
                return True
            elif keyword - 1000 < int(employee.rate) < keyword + 1000:
                return True
    return False


def search_multi(employee, word_list):
    res = []
    for word in word_list:
        res.append(search_keyword(employee, word))
    return all(res)

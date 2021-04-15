def question2(s):
    lst = list(s.upper())
    s1 = ""

    while len(lst) > 0:
        for j in ["W", "D", "L"]:
            if j in lst:
                s1 += j
                lst.remove(j)
    return s1


print(question2("ldwdl"))

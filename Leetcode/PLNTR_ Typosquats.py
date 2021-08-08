def typosquats(companyDomains, newDomains):
    result = []
    compD = [comp.split(".") for comp in companyDomains]
    newD = [new.split(".") for new in newDomains]

    for prefix, suffix in compD:

        for index, [prefix2, suffix2] in enumerate(newD):

            if prefix == prefix2 and suffix != suffix2:
                typo = newDomains[index]
                result.append(typo)

    print(result)


def normalizeDomain(arr):
    res = []
    for dom in arr:
        s = ""
        for letter in dom:
            if letter in ["1", "i", "l", "!", "|"]:
                s += "1"
            elif letter in ["s", "5", "$"]:
                s += "s"
            elif letter in ["o", "0"]:
                s += "o"
            elif letter in ["a", "@"]:
                s += "a"
            elif letter in ["e", "3"]:
                s += "e"
            else:
                s += letter
        res.append(s)

    print(res)
    return res


def typosquats2(companyDomains, newDomains):
    result = set()
    potentialIndex = []

    compD = [comp.split(".") for comp in companyDomains]
    newD = [new.split(".") for new in newDomains]

    normOld = normalizeDomain(companyDomains)
    normNew = normalizeDomain(newDomains)

    normalizeC = [norm.split(".") for norm in normOld]
    normalizeD = [norm.split(".") for norm in normNew]

    for prefix, suffix in normalizeC:
        for index, [prefix2, suffix2] in enumerate(normalizeD):

            if prefix == prefix2:
                # then we check again
                potentialIndex.append(index)

    for prefix, suffix in compD:
        for index, [prefix2, suffix2] in enumerate(newD):

            if index in potentialIndex:
                # ensures that the other entry in the outer loop doesn't add to the result
                if len(prefix) == len(prefix2):
                    if prefix != prefix2 or suffix != suffix2:
                        typo = newDomains[index]
                        result.add(typo)

    print(potentialIndex)
    print(list(result))


company = ["palantir.com", "apple.com"]
novel = ["palantir.biz", "apple.org", "apple.com", "appleorchard.net"]
#
# typosquats(company, novel)

# company = ["palantir.com", "nic.ci"]
# novel = ["paiantir.com", "palantir.com", "nic.cl", "palantirtechnologies.com", "nlc.biz"]

typosquats2(company, novel)

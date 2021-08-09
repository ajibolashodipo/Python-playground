FINAL = set()


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

    # print(res)
    return res


def swapSplit(domain):
    res = []
    domSplit = list(domain)

    for i in range(len(domSplit) - 1):
        j = i + 1

        copied = domSplit.copy()
        copied[j], copied[i] = copied[i], copied[j]
        swapped = "".join(copied)
        aSplit = swapped.split(".")[0]
        res.append(aSplit)

    # print(res)
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
                        FINAL.add(typo)


def typosquats3(companyDomains, newDomains):
    compD = [comp.split(".") for comp in companyDomains]
    res = []
    for prefix, suffix in compD:

        for dom in newDomains:

            prefixDom = dom.split(".")[0]
            # swapSplit

            prefixPermutations = swapSplit(dom)
            if prefix in prefixPermutations and prefix != prefixDom:
                res.append(dom)
                FINAL.add(dom)

            # this is the point to call other tsquat functions
            else:
                domList = [dom]
                typosquats2(companyDomains, domList)

    print(list(FINAL))
    return list(FINAL)


company = ["palantir.com", "apple.com"]
novel = ["palantir.com", "aplantirtechnologies.com", "palanti.rbiz"]

# company = ["palantir.com", "nic.ci"]
# novel = ["paiantir.com", "palantir.com", "nic.cl", "palantirtechnologies.com", "nlc.biz"]

typosquats3(company, novel)

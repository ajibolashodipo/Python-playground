def solution(s):
    s = list(s)
    digits = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8,
              "nine": 9}
    list_bag = []
    digit_keys = digits.keys()

    for digit in digit_keys:

        digit_list = list(digit)
        count = 0
        # to_del = []
        for el in digit_list:

            if el in s:
                count += 1

        # only update original list if you found a complete digit match
        if count == len(digit):
            # register completion by updating list_bag with found digit
            list_bag.append(digit)

            # update list by removing digit letters from original list
            updateList(s, digit)

    # initialize list
    numerical = []
    for j in list_bag:
        x = digits[j]
        numerical.append(x)

    numerical.sort()

    result = ''.join(map(str, numerical))
    print(result)
    return result


def updateList(s, digit):
    d = list(digit)

    for i in d:
        s.remove(i)


solution("reuonnoinfesixsevenntwozero") #149

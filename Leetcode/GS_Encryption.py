def encryptionValidity(instCount, validity, keys):
    maxi = 0
    keys.sort(reverse=True)
    for key in range(len(keys)):
        temp = 0
        for j in range(key, len(keys)):
            if keys[key] % keys[j] == 0:
                temp += 1
        maxi = max(temp, maxi)

    strength = maxi * 100000

    test = instCount * validity

    if strength < test:
        return 1, strength
    else:
        return 0, strength

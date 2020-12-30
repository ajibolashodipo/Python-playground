def happyLadybugs(b):
    # check if >=1 empty space exists and characters have more than one occurrence
    if b.count("_") >= 1:
        tracker = 0
        for a in set(b):
            if a == "_": continue
            if b.count(a) == 1: tracker += 1

        if tracker == 0: return "YES"

    # check for zero empty spaces and ordered
    if b.count("_") == 0:
        print("ajibola")
        tracker1 = 0
        for i in range(1, len(b) - 1):
            if b[i - 1] == b[i] or b[i] == b[i + 1]:
                tracker1 += 1
                print(tracker1)

        if tracker1 == len(b) - 2: return "YES"

    return "NO"


print(happyLadybugs("AABBAARR_"))

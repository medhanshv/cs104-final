import sys

var = 0
finalist = []

with open("translations.csv", "r") as file:
    for line in file:
        var += 1
        given = line.strip("\n")
        listed = given.split(',')
        finalist.append(listed)

# Initialize desired as a list of lists
desired = [[None] * 3 for _ in range(var)]

for i in range(var):
    if finalist[i][0] == "punjabi":
        if finalist[i][2] == "english":
            if finalist[i][1] not in sum(desired, []) and finalist[i][3] not in sum(desired, []):
                desired[i][1] = finalist[i][3]
                desired[i][2] = finalist[i][1]
            else:
                for j in range(var):
                    if finalist[i][1] in desired[j]:
                        desired[j][desired[j].index(finalist[i][1]) - 1] = finalist[i][3]
                        break
                    if finalist[i][3] in desired[j]:
                        desired[j][desired[j].index(finalist[i][3]) + 1] = finalist[i][1]
                        break

    if finalist[i][0] == "english":
        if finalist[i][2] == "punjabi":
            if finalist[i][1] not in sum(desired, []) and finalist[i][3] not in sum(desired, []):
                desired[i][2] = finalist[i][3]
                desired[i][1] = finalist[i][1]
            else:
                for j in range(var):
                    if finalist[i][1] in desired[j]:
                        desired[j][desired[j].index(finalist[i][1]) + 1] = finalist[i][3]
                        break
                    if finalist[i][3] in desired[j]:
                        desired[j][desired[j].index(finalist[i][3]) - 1] = finalist[i][1]
                        break

    if finalist[i][0] == "hindi":
        if finalist[i][2] == "english":
            if finalist[i][1] not in sum(desired, []) and finalist[i][3] not in sum(desired, []):
                desired[i][1] = finalist[i][3]
                desired[i][0] = finalist[i][1]
            else:
                for j in range(var):
                    if finalist[i][1] in desired[j]:
                        desired[j][desired[j].index(finalist[i][1]) + 1] = finalist[i][3]
                        break
                    if finalist[i][3] in desired[j]:
                        desired[j][desired[j].index(finalist[i][3]) - 1] = finalist[i][1]
                        break

    if finalist[i][0] == "english":
        if finalist[i][2] == "hindi":
            if finalist[i][1] not in sum(desired, []) and finalist[i][3] not in sum(desired, []):
                desired[i][0] = finalist[i][3]
                desired[i][1] = finalist[i][1]
            else:
                for j in range(var):
                    if finalist[i][1] in desired[j]:
                        desired[j][desired[j].index(finalist[i][1]) - 1] = finalist[i][3]
                        break
                    if finalist[i][3] in desired[j]:
                        desired[j][desired[j].index(finalist[i][3]) + 1] = finalist[i][1]
                        break

    if finalist[i][0] == "punjabi":
        if finalist[i][2] == "hindi":
            if finalist[i][1] not in sum(desired, []) and finalist[i][3] not in sum(desired, []):
                desired[i][0] = finalist[i][3]
                desired[i][2] = finalist[i][1]
            else:
                for j in range(var):
                    if finalist[i][1] in desired[j]:
                        desired[j][desired[j].index(finalist[i][1]) - 2] = finalist[i][3]
                        break
                    if finalist[i][3] in desired[j]:
                        desired[j][desired[j].index(finalist[i][3]) + 2] = finalist[i][1]
                        break

    if finalist[i][0] == "hindi":
        if finalist[i][2] == "punjabi":
            if finalist[i][1] not in sum(desired, []) and finalist[i][3] not in sum(desired, []):
                desired[i][2] = finalist[i][3]
                desired[i][0] = finalist[i][1]
            else:
                for j in range(var):
                    if finalist[i][1] in desired[j]:
                        desired[j][desired[j].index(finalist[i][1]) + 2] = finalist[i][3]
                        break
                    if finalist[i][3] in desired[j]:
                        desired[j][desired[j].index(finalist[i][3]) - 2] = finalist[i][1]
                        break

ans1 = []
if len(sys.argv) == 3 and sys.argv[1] == "1":
    if sys.argv[2] == "english":
        ans1 = sorted([desired[i][1] for i in range(var) if desired[i][1] is not None], reverse=True)
    if sys.argv[2] == "hindi":
        ans1 = sorted([desired[i][0] for i in range(var) if desired[i][0] is not None], reverse=True)
    if sys.argv[2] == "punjabi":
        ans1 = sorted([desired[i][2] for i in range(var) if desired[i][2] is not None], reverse=True)
    print(ans1)

ans2 = []
if len(sys.argv) == 4 and sys.argv[1] == "2":
    for i in range(var):
        if desired[i][0] is not None and desired[i][1] is not None:
            ans2.append((desired[i][0], desired[i][1]))
    if sys.argv[2] == "hindi" and sys.argv[3] == "english":
        print(sorted(ans2, key=lambda x: x[0]))
    elif sys.argv[2] == "english" and sys.argv[3] == "hindi":
        print(sorted([(b, a) for a, b in ans2], key=lambda x: x[0]))

    ans2 = [(desired[i][0], desired[i][2]) for i in range(var) if desired[i][0] is not None and desired[i][2] is not None]
    if sys.argv[2] == "hindi" and sys.argv[3] == "punjabi":
        print(sorted(ans2, key=lambda x: x[0]))
    elif sys.argv[2] == "punjabi" and sys.argv[3] == "hindi":
        print(sorted([(b, a) for a, b in ans2], key=lambda x: x[0]))

    ans2 = [(desired[i][2], desired[i][1]) for i in range(var) if desired[i][1] is not None and desired[i][2] is not None]
    if sys.argv[2] == "punjabi" and sys.argv[3] == "english":
        print(sorted(ans2, key=lambda x: x[0]))
    elif sys.argv[2] == "english" and sys.argv[3] == "punjabi":
        print(sorted([(b, a) for a, b in ans2], key=lambda x: x[0]))

if len(sys.argv) == 5 and sys.argv[1] == "3":
    found = False
    for i in range(var):
        if desired[i][1] == sys.argv[4]:
            print(desired[i][0] if sys.argv[3] == "hindi" else desired[i][2] if sys.argv[3] == "punjabi" else desired[i][1])
            found = True
        if desired[i][0] == sys.argv[4]:
            print(desired[i][0] if sys.argv[3] == "hindi" else desired[i][2] if sys.argv[3] == "punjabi" else desired[i][1])
            found = True
        if desired[i][2] == sys.argv[4]:
            print(desired[i][0] if sys.argv[3] == "hindi" else desired[i][2] if sys.argv[3] == "punjabi" else desired[i][1])
            found = True
    
    if not found:
        print("UNK")

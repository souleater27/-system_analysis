from io import StringIO
import math
import csv

def task(csvString):
    f = StringIO(csvString)
    reader = csv.reader(f, delimiter=',')
    out = []
    for row in reader:
        out.append(row)

    r1 = []
    [r1.append(i[0]) for i in out]
    r2 = []
    [r2.append(i[1]) for i in out]
    r3 = []


    for i in range(len(out)):
        for j in range(i+1, len(out)):
            if out[i][1] == out[j][0]:
                r3.append(out[i][0])
    r4 = []

    for i in range(len(out)):
        for j in range(i+1, len(out)):
            if out[i][1] == out[j][0]:
                r4.append(out[j][1])
    r5 = []

    for i in range(len(out)):
        for j in range(i+1, len(out)):
            if out[i][0] == out[j][0]:
                r5.append(out[i][1])
                r5.append(out[j][1])
    res = []
    v = set()

    for i in out:
        for j in i:
            v.add(int(j))
    max_v = max(v)
    v = sorted(v)


    for i in v:
        res.append([])
        res[i - 1].append(r1.count(str(i)))
        res[i - 1].append(r2.count(str(i)))
        res[i - 1].append(r3.count(str(i)))
        res[i - 1].append(r4.count(str(i)))
        res[i - 1].append(r5.count(str(i)))
    h = 0
    for i in range(len(v)):
        for j in range(int(max_v)):
            if res[i][j] != 0:
                h += res[i][j] * math.log(res[i][j] / (len(v) - 1), 2) / (len(v) - 1)
    h = -h
    return h


from io import StringIO
import csv


def task(csvString):
    f = StringIO(csvString)
    reader = csv.reader(f, delimiter=',')
    out = []
    for row in reader:
        out.append(row)
def task(csvString):
    f = StringIO(csvString)
    reader = csv.reader(f, delimiter=',')
    
    out = []
    for row in reader:
        out.append(row)
    
    # r1 - прямое управление
    r1 = []
    for x in out:
        if x[0] not in r1:
            r1.append(x[0])
    
    # r2 -прямое подчинение
    r2 = []
    for x in out:
        if x[1] not in r2:
            r2.append(x[1])

    # r3 -косвенное управление
    out3 = out
    r3 = []
    for x in out:
        for y in out3:
            if x[0] not in r3 and x[1] == y[0]:
                r3.append(x[0])

    # r4 - косвенное подчинение
    r4 = []
    for x in out:
        for y in out3:
            if y[1] not in r4 and x[0] == y[1]:
                r4.append(x[1])
                
    # r5 - соподчинение
    r5 = []
    for x in out:
        for y in out3:
            if x[1] not in r5 and x[0] == y[0]:
                r5.append(x[1])

    return [r1, r2, r3, r4, r5]

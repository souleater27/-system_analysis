import numpy as np
import json

def to_json(s):
    js = json.loads(s)
    s2 = []
    for j in js:
        if isinstance(j, list):
            s2.append(j)
        if isinstance(j, str):
            a = []
            a.append(j)
            s2.append(a)
    return s2

def exp_ind(arr, exam):
    ind = -1
    for i in range(len(exam)):
        if arr == exam[i]:
            ind = i
    return ind


def create_matrix(exam, index):
    exp = np.zeros((len(exam[index]), len(exam[index])))
    for i in range(len(exam[index])):
        for j in range(len(exam[index])):
            if exam[index][i] < exam[index][j]:
                exp[i][j] = 1
            if exam[index][i] == exam[index][j]:
                exp[i][j] = 0.5
            if exam[index][i] > exam[index][j]:
                exp[i][j] = 0
    return exp


def task(js):
    exam = to_json(js)
    exam_matr = []
    for exp in exam:
        exam_matr.append(create_matrix(exam, exp_ind(exp, exam)))

    m = np.zeros(exam_matr[0].shape)
    for i in range(exam_matr[0].shape[0]):
        for j in range(exam_matr[0].shape[0]):
            for k in range(len(exam_matr)):
                m[i][j] += 1 / exam_matr[k].shape[0] * exam_matr[k][i][j]

    k0 = []
    for i in range(exam_matr[0].shape[0]):
        k0.append(1 / exam_matr[0].shape[0])

    y = np.dot(m, k0)
    l = np.dot(np.array([1, 1, 1]), y)
    k1 = np.dot(1 / l, y)

    while max(abs(k1 - k0)) >= 0.001:
        k0 = k1
        y = np.dot(m, k0)
        l = np.dot(np.array([1, 1, 1]), y)
        k1 = np.dot(1 / l, y)

    return k1
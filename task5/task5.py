import json
import numpy as np

def task(ranking1_str, ranking2_str):
    ranking1 = json.loads(ranking1_str)
    ranking2 = json.loads(ranking2_str)

    mat1 = relationship_matrix(ranking1)
    mat1_t = y_a.transpose()

    mat2 = relationship_matrix(ranking2)
    mat2_t = y_b.transpose()

    mat3 = np.multiply(mat1, mat2)
    mat3_t = np.multiply(mat1_t, mat2_t)

    conflicts = []

    for i in range(mat3.shape[0]):
        for j in range(mat3[i].shape[1]):
            if int(mat3[i,j]) == 0 and int(mat3_t[i,j]) == 0:
                if [str(j+1),str(i+1)] not in conflicts:
                    conflicts.append([str(i+1),str(j+1)])

    return conflicts


def relationship_matrix(ranking):
    ranks = dict()
    rank_len = ranking_length(ranking)
    for i, rank in enumerate(ranking):
        if type(rank) is str:
            ranks[int(rank)] = i
        else:
            for r in rank:
                ranks[int(r)] = i

    return np.matrix([[1 if ranks[i+1] <= ranks[j+1] else 0 for j in range(rank_len)] for i in range(rank_len)])

def ranking_length(ranking) -> int:
    length = 0;
    for i in ranking:
        if type(i) is str:
            length+=1
        else:
            length+=len(i)
    return length


from numpy import *
from numpy.linalg import *
from math import sqrt


def svd(D):
    A = array(D)
    At = transpose(A)
    M = At @ A
    Eval, Evec = eig(M)
    for i in range(len(Eval)):
        for j in range(i + 1, len(Eval)):
            if Eval[j] > Eval[i]:
                Eval[i], Eval[j] = Eval[j], Eval[i]
                for k in range(len(Evec)):
                    Evec[k][i], Evec[k][j] = Evec[k][j], Evec[k][i]
    Eval_ = list(Eval)
    for i in range(len(Eval_)):
        if Eval_[i] < 0:
            Eval_[i] = 0
    if 0 in Eval_:
        r = Eval_.index(0)
    else:
        r = len(Eval_)
    Evals = [sqrt(Eval_[i]) for i in range(r)]
    Rvecs = []
    for i in Evec:
        Rvecs.append(i[:r])
    Lvecs = []
    for i in range(r):
        v = list((1/Evals[i]) * (A @ array(Rvecs)[:, i]))
        Lvecs.append(v)
    EVDiag = diag(array(Evals))
    RSvecs = array(Rvecs)
    LSvecs = transpose(array(Lvecs))
    return LSvecs, EVDiag, RSvecs

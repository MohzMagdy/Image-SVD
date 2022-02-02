from numpy import *
from numpy.linalg import *
from math import sqrt


def svd(D):                                                             # Taking the input matrix
    A = array(D)                                                        # Assuring the matrix is in the array form
    At = transpose(A)
    M = At @ A
    Eval, Evec = eig(M)
    for i in range(len(Eval)):                                          # Ordering the singular values in an ascending
        for j in range(i + 1, len(Eval)):                               # \\ manner, preserving their correspondence to
            if Eval[j] > Eval[i]:                                       # \\ their eigen vectors
                Eval[i], Eval[j] = Eval[j], Eval[i]
                for k in range(len(Evec)):
                    Evec[k][i], Evec[k][j] = Evec[k][j], Evec[k][i]
    Eval_ = list(Eval)
    for i in range(len(Eval_)):                                         # For very tiny negative values that might arise
        if Eval_[i] < 0:                                                # \\ from errors in the numerical calculations
            Eval_[i] = 0
    if 0 in Eval_:
        r = Eval_.index(0)
    else:
        r = len(Eval_)
    Evals = [sqrt(Eval_[i]) for i in range(r)]                          # Getting rid of zero values and corresponding
    Rvecs = []                                                          # \\ vectors
    for i in Evec:
        Rvecs.append(i[:r])
    Lvecs = []
    for i in range(r):
        v = list((1/Evals[i]) * (A @ array(Rvecs)[:, i]))
        Lvecs.append(v)
    EVDiag = diag(array(Evals))                                         # The final factorization form
    RSvecs = array(Rvecs)
    LSvecs = transpose(array(Lvecs))
    return LSvecs, EVDiag, RSvecs

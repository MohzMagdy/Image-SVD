from reducedSVD import *


def mtsvd(M):
    A = array(M)
    siz = shape(A)
    U, S, V = svd(A)
    Sval_ = list(diag(S))
    n = 0
    Alsum = sum(Sval_)
    r = len(Sval_)
    for i in range(len(Sval_)):
        n += Sval_[i]
        if n/Alsum > 0.8:
            r = i
            break
    Vr = V[:, :r].copy()
    Sr = diag(Sval_[:r].copy())
    Ur = U[:, :r].copy()
    return Ur, Sr, Vr

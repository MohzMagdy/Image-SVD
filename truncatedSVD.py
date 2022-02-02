from reducedSVD import *


def tsvd(M):
    A = array(M)
    siz = shape(A)
    U, S, V = svd(A)
    Sval_ = list(diag(S))
    B = siz[0] / siz[1]
    cp = 0.56 * (B ** 3) - 0.96 * (B ** 2) + 1.82 * B + 1.43
    med = median(Sval_.copy())
    n = len(Sval_)
    for i in range(len(Sval_)):
        if Sval_[i] < cp * med:
            n = i
            break
    Vr = V[:, :n].copy()
    Sr = diag(Sval_[:n].copy())
    Ur = U[:, :n].copy()
    return (Ur, Sr, Vr)

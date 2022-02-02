from reducedSVD import *


def mtsvd(M):                           # Getting the input matrix
    A = array(M)                        # Assuring its array form
    siz = shape(A)
    U, S, V = svd(A)                    # Getting its SVD factorization
    Sval_ = list(diag(S))
    n = 0
    Alsum = sum(Sval_)                  # The sum of all the singular values
    r = len(Sval_)
    for i in range(len(Sval_)):         # Determining the total needed intensity from the singular values
        n += Sval_[i]
        if n/Alsum > 0.8:
            r = i
            break
    Vr = V[:, :r].copy()                # The manually truncated SVD factors based on the specified intensity
    Sr = diag(Sval_[:r].copy())
    Ur = U[:, :r].copy()
    return Ur, Sr, Vr

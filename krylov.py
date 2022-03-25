import numpy as np
import lab2

def krylov(A: np.ndarray):
    np.set_printoptions(precision=5)
    n = A.shape[0]
    y = np.zeros((n + 1, n))
    y[0][0] = 1
    for i in range(1, n + 1):
        y[i] = A@y[i - 1]
    print('y = ', y)
    b = y[n]
    y = np.transpose(y[0:n])
    y = y[:, ::-1]
    p = lab2.gaus(y.tolist(), b.tolist())
    print('p = ', p)
    p = np.array(p)
    l = np.roots(np.concatenate(([1], -1 * p)))
    print('l = ', l)
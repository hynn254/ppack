import numpy as np
import scipy

def Tarvainen2002(signal, regularization=10):
    N = len(signal)

    identity = np.eye(N)
    B = np.dot(np.ones((N - 2, 1)), np.array([[1, -2, 1]]))
    D_2 = scipy.sparse.dia_matrix((B.T, [0, 1, 2]), shape=(N - 2, N))  # pylint: disable=E1101

    D_2_dense = D_2.toarray()
    D_2_row = D_2_dense.shape[0]
    D_2_col = D_2_dense.shape[1]
    D_2_dense[D_2_row - 2, D_2_col - 2] = 1
    D_2_dense[D_2_row - 1, D_2_col - 2] = -2
    D_2_dense[D_2_row - 1, D_2_col - 1] = 1

    inv = np.linalg.inv(identity + regularization ** 2 * D_2_dense.T @ D_2_dense)
    result = (identity - inv) @ signal

    return result
import sys

from backend import Matrix, read_rows_cols
from multiprocessing import Pool
from time import time

MAX_DIM = 100


def parallel_prod(A, B):
    assert (A.cols == B.rows)
    As = A.split(MAX_DIM)
    Bs = B.split(MAX_DIM)
    P = [[None] * len(Bs[0])] * len(As)
    return P


def main(test_no):
    m1_file = 'data/t_' + str(test_no) + '_m1.in'
    m2_file = 'data/t_' + str(test_no) + '_m2.in'
    out_file = 'data/s_' + str(test_no) + '.out'

    r1, c1 = read_rows_cols(m1_file)
    r2, c2 = read_rows_cols(m2_file)
    A = Matrix(1, r1, 1, c1)
    B = Matrix(1, r2, 1, c2)
    P = parallel_prod(A, B)
    P.write(out_file)


if __name__ == '__main__':
    start = time()

    try:
        test_no = int(sys.argv[1])
    except:
        print 'No test number provided. Default is 0.'
        test_no = 0
    main(test_no)

    end = time()
    print 'Done! It took ' + str(round(end - start, 4)) + ' seconds.'

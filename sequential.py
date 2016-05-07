from backend import *


TEST_NO = 1
M1_FILE = 'data/t_' + str(TEST_NO) + '_m1.in'
M2_FILE = 'data/t_' + str(TEST_NO) + '_m2.in'
OUT_FILE = 'data/t_' + str(TEST_NO) + '.out'


if __name__ == '__main__':
    r1, c1 = read_rows_cols(M1_FILE)
    r2, c2 = read_rows_cols(M2_FILE)
    M1 = Matrix(1, r1, 1, c1)
    M2 = Matrix(1, r2, 1, c2)
    M1.read(M1_FILE)
    M2.read(M2_FILE)
    P = prod(M1, M2)
    P.write(OUT_FILE)
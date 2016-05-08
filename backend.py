import numpy as np


class Matrix(object):

    def __init__(self, r1, r2, c1, c2):
        self.rows = r2 - r1 + 1
        self.cols = c2 - c1 + 1
        self.r1, self.r2, self.c1, self.c2 = (r1, r2, c1, c2)
        self.data = np.zeros((self.rows, self.cols), dtype=int)

    def split(self, dim):
        S = []
        for i in xrange(0, self.rows, dim):
            line = []
            for j in xrange(0, self.cols, dim):
                r1 = self.r1 + i * dim
                r2 = max(self.r2, self.r2 + (i+1) * dim)
                c1 = self.c1 + j * dim
                c2 = max(self.c2, self.c2 + (j+1) * dim)
                line.append(Matrix(r1, r2, c1, c2))
            S.append(line)
        return S

    def read(self, path):
        fp = open(path, 'r')
        for i, line in enumerate(fp):
            if i < self.r1:
                continue
            elif i > self.r2:
                break
            values = line.strip('\n').split(' ')
            values = map(int, values[(self.c1-1):self.c2])
            self.data[i-1] = np.array(values)
        fp.close()

    def write(self, path):
        fp = open(path, 'w')
        fp.write(str(self.rows) + ' ' + str(self.cols) + '\n')
        for i in xrange(self.rows):
            fp.write(' '.join(map(str, self.data[i])) + '\n')
        fp.close()


def read_rows_cols(path):
    fp = open(path, 'r')
    line = fp.readline()
    rows, cols = line.strip('\n').split(' ')
    return int(rows), int(cols)


def add(M1, M2):
    P = Matrix(1, M1.rows, 1, M1.cols)
    P.data = np.add(M1.data, M2.data)
    return P


def prod(M1, M2):
    P = Matrix(1, M1.rows, 1, M2.cols)
    P.data = np.dot(M1.data, M2.data)
    return P

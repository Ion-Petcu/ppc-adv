import numpy as np
from multiprocessing import Array


class SharedMatrix(object):

    def __init__(self, n, m, shared_array):
        self.rows = n
        self.cols = m
        self.shared_array = shared_array
        self.data = np.frombuffer(shared_array.get_obj(), dtype=int).reshape((n, m))

    @property
    def params(self):
        return self.rows, self.cols, self.shared_array

    @classmethod
    def read(cls, path):
        fp = open(path, 'r')
        n, m = (0, 0)
        shared_array = None
        for i, line in enumerate(fp):
            if i == 0:
                n, m = map(int, line.strip('\n').split(' '))
                shared_array = Array('l', n * m)
                continue
            shared_array[(i - 1) * m: i * m] = map(int, line.strip('\n').split(' '))
        fp.close()
        return cls(n, m, shared_array)

    def write(self, path):
        fp = open(path, 'w')
        fp.write(str(self.rows) + ' ' + str(self.cols) + '\n')
        for i in xrange(self.rows):
            fp.write(' '.join(map(str, self.data[i])) + '\n')
        fp.close()

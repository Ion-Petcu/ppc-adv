import numpy as np
import sys
import time
from timeit import default_timer as timer

WITH_NP = False

def read(path):
    fp = open(path, 'r')
    m = []
    for i, line in enumerate(fp):
        if i == 0:
            continue
        m.append(map(int, line.strip('\n').split(' ')))
    fp.close()
    return np.array(m)


def write(m, path):
    rows, cols = m.shape
    fp = open(path, 'w')
    fp.write(str(rows) + ' ' + str(cols) + '\n')
    for i in xrange(rows):
        fp.write(' '.join(map(str, m[i])) + '\n')
    fp.close()


def main(test_no):
    m1_file = 'data/t_' + str(test_no) + '_m1.in'
    m2_file = 'data/t_' + str(test_no) + '_m2.in'
    out_file = 'data/s_' + str(test_no) + '.out'

    a = read(m1_file)
    b = read(m2_file)

    # c = np.zeros((a.shape[0], b.shape[1]))
    if WITH_NP:
        start = timer()
        c = np.dot(a, b)

    else:
        c = np.zeros((a.shape[0], b.shape[1]), dtype=int)
        start = timer()
        for row in xrange(a.shape[0]):
            for col in xrange(b.shape[1]):
                c[row, col] = sum(a[row] * b[:, col])

    end = timer()

    write(c, out_file)
    return round(end - start, 4)


if __name__ == '__main__':
    try:
        test_no = int(sys.argv[1])
    except:
        print 'No test number provided. Default is 0.'
        test_no = 0
    seconds = main(test_no)
    print 'Done! It took ' + str(seconds) + ' seconds.'

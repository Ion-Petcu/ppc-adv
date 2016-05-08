import sys
import time
from multiprocessing import Process, cpu_count
import numpy as np
from backend import SharedMatrix

def compute(workers_num, proc_index,
            m1_rows, m1_cols, m1_buffer,
            m2_rows, m2_cols, m2_buffer,
            c_rows, c_cols, c_buffer):
    m1 = SharedMatrix(m1_rows, m1_cols, m1_buffer)
    m2 = SharedMatrix(m2_rows, m2_cols, m2_buffer)
    c = SharedMatrix(c_rows, c_cols, c_buffer)
    for out_line in xrange(proc_index, c.rows, workers_num):
        c.data[out_line] = np.dot(m1.data[out_line], m2.data)
        # for out_col in xrange(c.cols):
        #     c.data[out_line, out_col] = sum(m1.data[out_line] * m2.data[:, out_col])


def main(test_no):
    m1_file = 'data/t_' + str(test_no) + '_m1.in'
    m2_file = 'data/t_' + str(test_no) + '_m2.in'
    out_file = 'data/p_' + str(test_no) + '.out'

    m1 = SharedMatrix.read(m1_file)
    m2 = SharedMatrix.read(m2_file)
    c = SharedMatrix(m1.params[0], m2.params[1])

    try:
        workers_num = cpu_count()
    except NotImplementedError:
        workers_num = 4

    processes = []
    for i in xrange(workers_num):
        processes.append(Process(target=compute, args=((workers_num, i) + m1.params + m2.params + c.params)))

    start = time.time()
    for process in processes:
        process.start()
    for process in processes:
        process.join()
    end = time.time()
    c.write(out_file)

    return round(end - start, 4)


if __name__ == '__main__':
    try:
        test_no = int(sys.argv[1])
    except:
        print 'No test number provided. Default is 0.'
        test_no = 0
    seconds = main(test_no)
    print 'Done! It took ' + str(seconds) + ' seconds.'

import sys
import time
from timeit import default_timer as timer
from multiprocessing import Process, cpu_count
import numpy as np
from backend import SharedMatrix

WITH_NP = False

def compute(workers_num, proc_index,
            m1_rows, m1_cols, m1_buffer,
            m2_rows, m2_cols, m2_buffer,
            c_rows, c_cols, c_buffer):
    m1 = SharedMatrix(m1_rows, m1_cols, m1_buffer)
    m2 = SharedMatrix(m2_rows, m2_cols, m2_buffer)
    c = SharedMatrix(c_rows, c_cols, c_buffer)
    if WITH_NP:
        c.data[xrange(proc_index, c.rows, workers_num)] = np.dot(
            m1.data[xrange(proc_index, c.rows, workers_num)],
            m2.data)
    else:
        for out_line in xrange(proc_index, c.rows, workers_num):
            # c.data[out_line] = np.dot(m1.data[out_line], m2.data)
            for out_col in xrange(c.cols):
                c.data[out_line, out_col] = sum(m1.data[out_line] * m2.data[:, out_col])


def main(test_no, parallelism):
    m1_file = 'data/t_' + str(test_no) + '_m1.in'
    m2_file = 'data/t_' + str(test_no) + '_m2.in'
    out_file = 'data/p_' + str(test_no) + '.out'

    m1 = SharedMatrix.read(m1_file)
    m2 = SharedMatrix.read(m2_file)
    c = SharedMatrix(m1.params[0], m2.params[1])

    if parallelism == None:
        try:
            workers_num = cpu_count()
        except NotImplementedError:
            workers_num = 4
    else:
        workers_num = parallelism

    processes = []
    for i in xrange(workers_num):
        processes.append(Process(target=compute, args=((workers_num, i) + m1.params + m2.params + c.params)))

    start = timer()
    for process in processes:
        process.start()
    for process in processes:
        process.join()
    end = timer()
    c.write(out_file)

    return round(end - start, 4)


if __name__ == '__main__':
    parallelism = None
    try:
        test_no = int(sys.argv[1])
        if len(sys.argv) >= 3:
            parallelism = int(sys.argv[2])
    except:
        print 'No test number provided. Default is 0.'
        test_no = 0
    seconds = main(test_no, parallelism)
    print 'Done! It took ' + str(seconds) + ' seconds.'

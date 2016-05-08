import sys
import time


def main(test_no):
    m1_file = 'data/t_' + str(test_no) + '_m1.in'
    m2_file = 'data/t_' + str(test_no) + '_m2.in'
    out_file = 'data/p_' + str(test_no) + '.out'

    start = time.time()
    # computation
    end = time.time()

    return round(end - start, 4)


if __name__ == '__main__':
    try:
        test_no = int(sys.argv[1])
    except:
        print 'No test number provided. Default is 0.'
        test_no = 0
    seconds = main(test_no)
    print 'Done! It took ' + str(seconds) + ' seconds.'

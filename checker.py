import sys


def read(path):
    fp = open(path, 'r')
    m = []
    for i, line in enumerate(fp):
        if i == 0:
            continue
        m.append(map(int, line.strip('\n').split(' ')))
    fp.close()
    return m


def main(test_no):
    s_file = 'data/s_' + str(test_no) + '.out'
    p_file = 'data/p_' + str(test_no) + '.out'
    s = read(s_file)
    p = read(p_file)
    if s == p:
        print 'OK!'
    else:
        print 'NOT OK!'


if __name__ == '__main__':
    try:
        test_no = int(sys.argv[1])
    except:
        print 'No test number provided. Default is 0.'
        test_no = 0
    main(test_no)

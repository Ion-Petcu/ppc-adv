import random


def generate_tests():
    ns = [10, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
    for t, n in enumerate(ns):
        generate_test(t, n)


def generate_test(test, n):
    m1_file = 'data/t_' + str(test) + '_m1.in'
    m2_file = 'data/t_' + str(test) + '_m2.in'
    generate_to_file(m1_file, n, n)
    generate_to_file(m2_file, n, n)


def generate_to_file(path, n, m):
    fp = open(path, 'w')
    fp.write(str(n) + ' ' + str(m) + '\n')
    for i in xrange(n):
        line = ' '.join(str(random.randint(1, 9)) for _ in xrange(m))
        fp.write(line + '\n')
    fp.close()


if __name__ == '__main__':
    generate_tests()

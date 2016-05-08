import random


def generate_tests(small, big):
    for t in xrange(small+big):
        min_dim = 10 if t < small else 8000
        max_dim = 1000 if t < small else 10000
        generate_test(t, min_dim, max_dim)


def generate_test(test, min_dim, max_dim):
    M1_FILE = 'data/t_' + str(test) + '_m1.in'
    M2_FILE = 'data/t_' + str(test) + '_m2.in'
    n = random.randint(min_dim, max_dim)
    m = random.randint(min_dim, max_dim)
    p = random.randint(min_dim, max_dim)
    generate_to_file(M1_FILE, n, m)
    generate_to_file(M2_FILE, m, p)


def generate_to_file(path, n, m):
    fp = open(path, 'w')
    fp.write(str(n) + ' ' + str(m) + '\n')
    for i in xrange(n):
        line = ' '.join(str(random.randint(0, 9)) for _ in xrange(m))
        fp.write(line + '\n')
    fp.close()


if __name__ == '__main__':
    generate_tests(5, 5)

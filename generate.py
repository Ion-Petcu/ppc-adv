import random


def generate_tests():
    tests = 4
    min_dim = [1, 10, 100, 1000, 2000, 3000, 4000, 5000]
    max_dim = [10, 100, 1000, 2000, 3000, 4000, 5000, 6000]
    for t in xrange(tests):
        generate_test(t, min_dim[t], max_dim[t])


def generate_test(test, min_dim, max_dim):
    m1_file = 'data/t_' + str(test) + '_m1.in'
    m2_file = 'data/t_' + str(test) + '_m2.in'
    n = random.randint(min_dim, max_dim)
    m = random.randint(min_dim, max_dim)
    p = random.randint(min_dim, max_dim)
    generate_to_file(m1_file, n, m)
    generate_to_file(m2_file, m, p)


def generate_to_file(path, n, m):
    fp = open(path, 'w')
    fp.write(str(n) + ' ' + str(m) + '\n')
    for i in xrange(n):
        line = ' '.join(str(random.randint(1, 9)) for _ in xrange(m))
        fp.write(line + '\n')
    fp.close()


if __name__ == '__main__':
    generate_tests()

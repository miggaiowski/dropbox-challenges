import random

NINST = 0

def inst(n):
    global NINST
    f = open('sss%02d' % NINST, 'w')
    NINST += 1
    f.write("%d\n" % n)
    for i in xrange(n):
        f.write("%d %d\n" % (i, random.randint(-2000, 2000)))
    f.close()

for i in xrange(30):
    inst(400)


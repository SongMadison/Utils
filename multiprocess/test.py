#from pathos.pools import ProcessPool as Pool

import multiprocessing
from multiprocessing import Pool
class someClass(object):
    def __init__(self):
        pass
    def f(self, x):
        return x*x
    def go(self):
        pool = Pool(4)
        print (pool.map(self.f, range(10)) )

sc = someClass()
print(sc.go())


class Foo():
    @staticmethod
    def work(self):
        pass

if __name__ == '__main__':   
    pool = Pool()
    foo = Foo()
    pool.apply_async(foo.work)
    pool.close()
    pool.join()
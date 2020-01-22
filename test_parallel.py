import multiprocessing
from multiprocessing import Process
from multiprocessing import Pool
import os

def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())

def f(name):
    info('function f')
    print('hello >>>>>> ', name)
    return name
if __name__ == '__main__':
    info('main line')
    num_of_cpu = multiprocessing.cpu_count()
    print("Number of cpu: "+str(num_of_cpu))
    with Pool(100) as p:
        print(p.map(f, list('abcdefghijklmnopqrstuvwxyz')*10))

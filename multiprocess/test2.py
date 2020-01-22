import os
from multiprocess import Pool #more stable than multiprocessing.Pool when handling with pickle issues
import dill


def run_dill_encoded(payload):
    fun, args = dill.loads(payload)
    return fun(*args)


def apply_async(pool, fun, args):
    payload = dill.dumps((fun, args))
    return pool.apply_async(run_dill_encoded, (payload,))


if __name__ == "__main__":

    pool = Pool(processes=5)

    # asyn execution of lambda
    jobs = []
    for i in range(10):
        job = apply_async(pool, lambda a, b: (a, b, a * b), (i, i + 1))
        jobs.append(job)
    print(jobs)
    for job in jobs:
        print (job.get())

    try:
        result = pool.map(lambda a: (a, a * a), range(10) )
        print(result)
    except Exception as e:
        print(str(e))
    # async execution of static method

    class O(object):

        @staticmethod
        def calc():
            return os.getpid()

    jobs = []
    for i in range(10):
        job = apply_async(pool, O.calc, ())
        jobs.append(job)

    for job in jobs:
        print (job.get())

    print("--------")
    try:
        result = pool.map(O.calc, ())
        print(result)
    except Exception as e:
        print("--------")
        print(str(e))

 





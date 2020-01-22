
# 1. Explanation about the picking issue in multiprocessing package
https://medium.com/@jwnx/multiprocessing-serialization-in-python-with-pickle-9844f6fa1812

introduction to pickle
https://docs.python.org/3/library/pickle.html#what-can-be-pickled-and-unpickled

stackoverflow about the issue
https://stackoverflow.com/questions/8804830/python-multiprocessing-picklingerror-cant-pickle-type-function

# 2. Parallel Processing in Python – A Practical Guide with Examples
https://www.machinelearningplus.com/python/parallel-processing-python/

# 3. Solutions:
1. using multiproces package instread of multiprocessing, both are in the standard python library
https://pypi.org/project/multiprocess/, a fork of multiprocessing package, better in handling picking issue. not completely
2. use library https://github.com/uqfoundation/pathos
3. write your script to do the pickle 
4. using TreadPool, which doesn't use pickle
from multiprocess.pool import ThreadPool
or 
from multiprocessing.pool import ThreadPool


# 4 differences between therad and processes



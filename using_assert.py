import sys
assert sys.argv[1] in ['train', 'test'], print("first parameter has to be 'train' or 'test' ")
IS_TEST = (sys.argv[1] == 'test')
if IS_TEST:
    print("creating test set")
else:
    print("creating train set")


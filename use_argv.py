import sys

def main():
    # print command line arguments
    for arg in sys.argv[1:]:
        print arg

if __name__ == "__main__":
    main()

'''
$ python cmdline_args.py arg1 arg2 arg3
arg1
arg2
arg3   
'''

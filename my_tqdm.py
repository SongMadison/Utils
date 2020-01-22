from tqdm import tqdm
import time

##reference:   https://github.com/tqdm/tqdm

######################################################################### 
#1. Iterable-based
######################################################################### 

for i in tqdm(range(int(1e8))):
    continue


text = ""
for char in tqdm(["a", "b", "c", "d"]):
    time.sleep(0.25)
    text = text + char

#trange(i) is a special optimised instance of tqdm(range(i)):

for i in trange(100):
    time.sleep(0.01)



#Instantiation outside of the loop allows for manual control over tqdm():

pbar = tqdm(["a", "b", "c", "d"])
for char in pbar:
    time.sleep(0.25)
    pbar.set_description("Processing %s" % char)

######################################################################### 
#Manual control on tqdm() updates by using a with statement:
######################################################################### 
#If the optional variable total (or an iterable with len()) is provided, predictive stats are displayed.
with tqdm(total=100) as pbar:
    for i in range(10):
        time.sleep(0.1)
        pbar.update(10)


#Equivalent to
pbar = tqdm(total=100)
for i in range(10):
    time.sleep(0.1)
    pbar.update(10)
pbar.close()



######################################################################### 
## commandline used in the pipe
######################################################################### 
#Perhaps the most wonderful use of tqdm is in a script or on the command line. Simply inserting tqdm (or python -m tqdm) between pipes will pass through all stdin to stdout while printing progress to stderr.
#it can also be used in the pipe
`seq 9999999 | tqdm --bytes | wc -l`
#import logging

#log = logging.getLogger("my-logger")
#log.info("Hello, world")



#https://www.loggly.com/ultimate-guide/python-logging-basics/
#In general, a module should emit log messages as a best practice and should not configure how those messages are handled. 
# That is the responsibility of the application.


#The only responsibility modules have is to make it easy for the application to route their log messages. 
# For this reason, it is a convention for each module to simply use a logger named like the module itself. 
# This makes it easy for the application to route different modules differently, while also keeping log code in the module simple. 
# The module just needs two lines to set up logging, and then use the named logger:


import logging
logger = logging.getLogger("testing")
logger.setLevel(logging.DEBUG)

fh = logging.FileHandler('simple_test.log')
fh.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)

def do_something():
    logger.debug("Doing something!")

if __name__=='__main__':
    do_something()
    logger.info('hello')
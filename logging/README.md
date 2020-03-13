


1. A log of good usage examples: https://docs.python.org/3/howto/logging.html
    1. `logging.basicConfig(filename='example.log', filemode='w', level=logging.DEBUG)`
    2. how to log into a file
    3. how to format the output
    4. how to set the level; default level is "WARNING", need to setting to "INFO" or "DEBUG"

2. how to log from multiple modules (the exapmle is copied from here: https://docs.python.org/3/howto/logging-cookbook.html)
module-lever logger, in each module which uses logging, named as follows:
    ```logger = logging.getLogger(__name__)```
This means that logger names track the package/module hierarchy, and it’s intuitively obvious where events are logged just from the logger name.

However, as mentioned here: https://stackoverflow.com/questions/50714316/how-to-use-logging-getlogger-name-in-multiple-modules
the logger has a hierachy, which musted be defined explicitly in the logger name, using dot-notation.

In the example here, the logger name in the `main_module.py` is `spam_application`;
then the logger name in `auxiliary_mode.py` must be `spam_application.xx`

3. Logging variable data
```python
import logging
logging.warning('%s before you %s', 'Look', 'leap!')
```
will display:

```
WARNING:root:Look before you leap!
```

4. Another good pratices: https://www.loggly.com/ultimate-guide/python-logging-basics/
    1. practice 1: setting logging levels
    2. practice 2: logging from mudule `logging.getLogger(__name__)`
    3. configuring logging:  In general, a configuration consists of adding a Formatter and a Handler to the root logger.  Applications should configure logging as early as possible, preferably as the first thing in the application, so that log messages do not get lost during startup. Finally, applications should wrap a try/except block around the main application code to send any exceptions through the logging interface instead of just to stderr
example:  see the `excetpion.py`

5. Difference between filehandler and console handler.
A: as in `log_to_a_file.py` shows, the filehandler allows the information print out to a file while console handler allows the information print to the console/command line. It can be enable for both.

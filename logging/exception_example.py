import logging
import os

class OneLineExceptionFormatter(logging.Formatter):
    def formatException(self, exc_info):
        result = super().formatException(exc_info)
        return repr(result)
 
    def format(self, record):
        result = super().format(record)
        if record.exc_text:
            result = result.replace("\n", "")
        return result
 
fh = logging.FileHandler('exception.log')
fh.setLevel(logging.DEBUG)
handler = logging.StreamHandler()

formatter = OneLineExceptionFormatter(logging.BASIC_FORMAT)
handler.setFormatter(formatter)

logger = logging.getLogger()
logger.setLevel(os.environ.get("LOGLEVEL", "INFO"))
logger.addHandler(fh)
logger.addHandler(handler)

 
try:
    exit(main())
except Exception:
    logging.exception("Exception in main(): ")
    #logger.error("Exception in main(): ", exc_info=True)
    #exit(1)

#logging.exception is shorthand equivalent to logging.error(..., exc_info=True).
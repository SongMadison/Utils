from datetime import datetime

datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
#'2023-02-16-17-53-32
datetime.now().strftime('%Y-%m-%d')
# '2023-02-16'


import datetime
import pytz

utc_now = pytz.utc.localize(datetime.datetime.utcnow())
pst_now = utc_now.astimezone(pytz.timezone("America/Los_Angeles"))
pst_now == utc_now
# > True
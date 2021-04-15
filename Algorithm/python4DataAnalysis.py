#Python4DataAnalysis
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
now = datetime.now()
now.year, now.month, now.day

delta = datetime(2011, 1, 7) - datetime(2008, 6, 24, 8, 15)
delta
delta.days 
delta.seconds

from datetime import timedelta
start = datetime(2011, 1, 7)
dt2 = start + timedelta(12)
dt3 = start - 2 * timedelta(12)
dt2.days
value = "2011-01-03"
datetime.strptime(value, '%Y-%m-%d')

#create time-series:
from datetime import datetime
dates = [datetime(2011, 1, 2), datetime(2011, 1, 5),
         datetime(2011, 1, 7), datetime(2011, 1, 8),
         datetime(2011, 1, 10), datetime(2011, 1, 12)]
ts = pd.Series(np.random.randn(6), index=dates)
ts # column: datetime, value

intervals = [[9, 10], [4, 9], [4, 17]]

heaps = []
intervals = sorted(intervals, key = lambda X: (X[0], X[1]), reverse = False)
for interval in intervals:
    if not heap:
        heappush(heaps, interval)
    elif interval[0] >= heaps[-1][1]:
        heaps[-1][1] = interval[1]
    else:
        heappush(heaps, interval)
return len(heaps)


from datetime import timedelta
start = datetime(2011, 1, 7)
dt2 = start + timedelta(12)
dt3 = start - 2 * timedelta(12)
dt2.days
value = "2011-01-03"

datetime.striptime(value, '%Y-%m-%d')












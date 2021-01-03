import pandas as pd


count = 0
dates = pd.date_range('1901-01-01', '2000-12-31', freq='1M')-pd.offsets.MonthBegin(1)
for date in dates:
    if date.weekday() == 6:
        count += 1

print(count)
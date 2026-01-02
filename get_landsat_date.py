import datetime
EPOCH_START = datetime.date(2000, 1, 6)
date = datetime.date.today()

num_days_delta = date - EPOCH_START
num_days = num_days_delta.days
landsat_date = num_days % 16 + 1
print(landsat_date)
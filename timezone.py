import datetime
import pytz


dt=datetime.datetime.now(tz=pytz.UTC)


dt_m=dt.astimezone(pytz.timezone('Etc/GMT+7'))

print(dt_m)
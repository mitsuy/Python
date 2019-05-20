########################################
#
#   How to get time or date.
#
#
#
#  Written by M.Yagyu 10 May 2019
#
########################################


import datetime as dtime

today=dtime.date.today()
today_detail=dtime.datetime.today()


###
### Todays date
###
print("----------------------------")
print(today)
print(today_detail)


###
### Todays date: every values
###

print("-----------------------------")
print(today.month,today.day,today.year)
print(today_detail.hour,':',today_detail.minute,':',today_detail.second,'.',today_detail.microsecond)


###
### Format for date
###

print("---------------------------------")
print(today.isoformat())
print(today_detail.strftime("%m-%d, %Y, %H:%M:%S"))



###
### Calculation of date
###

print("Tommorow date")
print(today_detail+dtime.timedelta(days=1))

year=dtime.datetime(2019,1,1)

print("Date difference from 2019-1-1 to today.")
calc=today_detail-year
print(calc.days)


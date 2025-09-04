seconds = int(input("How many seconds?: "))

sec_min = 60
sec_hr = 60 * sec_min
sec_day = 24 * sec_hr
sec_yr = 365 * sec_day

# this calculates the years
yr = seconds // sec_yr
seconds = seconds % sec_yr

#this calculates the days
day = seconds // sec_day
seconds = seconds % sec_day

# this calculates the hours
hr = seconds // sec_hr
seconds = seconds % sec_hr

# this calculates the minutes
minute = seconds // sec_min
seconds = seconds % sec_min

#leftover seconds
sec = seconds

print("Years:", yr)
print("Days:", day)
print("Hours:", hr)
print("Minutes:", minute)
print("Seconds:", sec)


import datetime

# The next 3 lines of code just demostrate constants.
print("-------------------------------")

#The smallest year number allowed in a date or datetime object. MINYEAR is 1.
print(datetime.MINYEAR)
print("-------------------------------")

#The largest year number allowed in a date or datetime object. MAXYEAR is 9999.
print(datetime.MAXYEAR)
print("-------------------------------")

#Alias for the UTC timezone singleton datetime.timezone.utc.
print(datetime.timezone.utc, end="\n\n")
print("-------------------------------")

# Printing today's date
today = datetime.datetime.today()

print("Today's date is", today)
print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)
print("Current seccond:", today.second)
print("Current miliseccond:", today.microsecond, end="\n\n")
print("-------------------------------")


# Difference between .date  .time   .datetime
Launch_date = datetime.date(2017, 3, 30)
Launch_time = datetime.time(22, 2, 0)
Lauch_datetime = datetime.datetime(2017, 3, 30, 22, 2, 0)
print(f"Result of .date: {Launch_date}.     Result of .time: {Launch_time}.     Result of .datetime: {Lauch_datetime}", end="\n\n")
print("-------------------------------")

# birthday of python creator + printing 1956-01-31 as: Tuesday, January, 31, 1956
gvr = datetime.date(1956, 1, 31)
print(gvr)
print(gvr.strftime("%A, %B, %d, %Y"), end="\n\n")       # %A: Weekday full name. %B: Month full name, %d: Date of the month, %Y: Year 56 as 0056
# %a: Weekday abriviated. %b: Month abvriviated, %y: Year 56 as 56
print("-------------------------------")

# Finding the date 100 days after 2000-1-1
mill = datetime.date(2000, 1, 1)
dt = datetime.timedelta(100)  #timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
print(f"The date 100 days after {mill} is {mill + dt}", end="\n\n")
print("-------------------------------")

# converting 7/20/1969 to
moon_landing = "7/20/1969"
moon_landing_datetime = datetime.datetime.strptime(moon_landing, "%m/%d/%Y")
print(moon_landing_datetime, end="\n\n")
print("-------------------------------")

# Time since Covid-19 was declared a global health emergency and was declared no longer an emergency.
began = datetime.date(2020, 1, 30)
end = datetime.date(2023, 5, 5)

df = end - began
print(df)
print("-------------------------------")
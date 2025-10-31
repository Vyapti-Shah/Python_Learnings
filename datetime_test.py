import datetime

date = datetime.date(2023, 5, 17)
print("Date:", date)
print()

today = datetime.date.today()
print("Today's Date:", today)
print()

time = datetime.time(14, 30, 0)
print("Time:", time)
print()

now = datetime.datetime.now()
print("Current Date and Time:", now)
print("Formatted:", now.strftime("%Y-%m-%d %H:%M:%S"))
print()

datetime_combined = datetime.datetime(2023, 5, 17, 14, 30, 0)
print("Datetime:", datetime_combined)
print()

target_date = datetime.date(2024, 1, 1)
current_date = datetime.date.today()
if target_date < current_date:
    print(f"{target_date} is in the past.")
else:
    print(f"{target_date} is in the future.")
import time

#epoch = a date and time from which a computer measures system time 
print(time)
print(time.ctime(0)) # convert a time expressed in seconds since epoch to a readable string

print(time.ctime(1000000)) # convert a time expressed in seconds since epoch to a readable string

print(time.time()) # return current seconds since epoch

print(time.ctime(time.time())) # returns current date and time

time_object = time.localtime()
time_utc = time.gmtime()
print(time_object)
print(time_utc) #Coordinated Universal Time 
local_time = time.strftime("%B %d %Y %H:%M:%S",time_object) # str-string f-format 
print(local_time)

time_string = "13 April, 2005"
time_birth = time.strptime(time_string, "%d %B, %Y")
print(time_birth)

# (year, month, day, hours, minutes, seconds, day of the week, day of the year, daylight saving time(dst))
time_tuple = (2024, 4, 13, 12, 12, 12, 0, 0, 0)
time_str = time.asctime(time_tuple)
print(time_str)
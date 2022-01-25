num=int(120)

def convert_to_time(num):

    hour = num//60
    return hour
hour = convert_to_time(num)

def Convert_to_time(num):
    minute = num%60
    return minute
minute = Convert_to_time(num)
if hour == 1 and minute == 1:

    print(hour, "hour", minute, "minute")

elif hour > 1 and minute == 1:

    print(hour, "hours", minute, "minute")

elif hour == 1 and minute > 1:

    print(hour, "hour", minute, "minutes")

elif hour > 1 and minute > 1:

    print(hour, "hours", minute, "minutes")

elif hour < 1 and minute> 1:
    print(minute, "minutes")

elif hour == 1 and minute <1:
    print(hour, "hour")
    
elif hour > 1 and minute < 1:
    print(hour, "hours")

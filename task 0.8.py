def convert_to_time(num):
  hour = num//60
  if hour==1:
   hour_string='hour'
  else:
    hour_string='hours'

  minutes=num-(hour*60) 
  if minutes==1:
    minute_string='minute'
  else:
    minute_string='minutes'

  print(str(hour)+''+str(hour_string)+''+str(minutes)+''+str(minute_string))
convert_to_time(163)

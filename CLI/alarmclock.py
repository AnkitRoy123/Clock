import time
try:
 a = int(input("Hour(0-23): "))
 b = int(input("Minute(0-59): "))
 while True:
    ct = time.localtime()
    hour = ct.tm_hour
    minute = ct.tm_min
    print(time.strftime("%H:%M:%S"), end="\r")
    time.sleep(1)
    if hour == a and minute == b:
      print("\nWake up.")
      for i in range(5):
       print('\a')
      break
except ValueError:
   print("Please enter a valid time..")

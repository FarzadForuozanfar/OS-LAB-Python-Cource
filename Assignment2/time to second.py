time = input("Enter Your time like 10:36:10 :")

hour, minute, second =time.split(":")

sec=int(hour)*3600 + int(minute)*60+ int(second)

print(sec)
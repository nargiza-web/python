# 5. Work or Sleep In?
# Prompt the user for a day of the week just like the previous problem. Except this time print "Go to work" if it's a work day and "Sleep in" if it's a weekend day. Example session:
# $ python work_or_sleep_in.py 
# Day (0-6)? 5 
# Go to work 
# $ python work_or_sleep_in.py 
# Day (0-6)? 6 
# Sleep in
#----------------------------

day = int(input('Day (0-6)?'))
if day>=1 and day<=5:
    print ('Go to work')
else:
    print ('Sleep in')
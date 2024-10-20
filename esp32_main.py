# This code hasen't been Tested
import machine
from time import sleep
from datetime import datetime

pin1=17  # 5V LED
pin2=27  # 220V RGB/bulb
# pin3=22  # 220V Power switch

switch1=machine.Pin(pin1,machine.Pin.OUT)
switch2=machine.Pin(pin2,machine.Pin.OUT)
# switch3 = machine.Pin(pin3, machine.Pin.OUT)

switch1.value(0)
switch2.value(0)
# switch3.value(0)

# Time for 220V Power on/off (for future use)
on_time_p=datetime.strptime("17:00:00", "%H:%M:%S").time()
off_time_q=datetime.strptime("23:00:00", "%H:%M:%S").time()

# Time for 5V LED
on_time_morning=datetime.strptime("07:00:00", "%H:%M:%S").time()
off_time_morning=datetime.strptime("09:00:00", "%H:%M:%S").time()
on_time_night=datetime.strptime("17:30:00", "%H:%M:%S").time()
off_time_night=datetime.strptime("19:00:00", "%H:%M:%S").time()

# Time for 220V bulb
on_time_1=datetime.strptime("18:00:00", "%H:%M:%S").time()
off_time_2=datetime.strptime("20:45:00", "%H:%M:%S").time()
on_time_3=datetime.strptime("21:15:00", "%H:%M:%S").time()
off_time_4=datetime.strptime("22:15:00", "%H:%M:%S").time()

try:
    while True:
        # Get current time
        current_time = datetime.now().time()
        ##### For 5V Temple LED (morning and night) #####
        if (on_time_morning<=current_time<=off_time_morning) or (on_time_night<=current_time<=off_time_night):
            switch1.value(1)
        else:
            switch1.value(0)

        ##### For 220V Study Bulb #####
        if (on_time_1<=current_time<=off_time_2) or (on_time_3<=current_time<=off_time_4):
            switch2.value(1)
        else:
            switch2.value(0)

        ##### For 220V Power Switch (uncomment in future use) #####
        '''
        if on_time_p <= current_time <= off_time_q:
            switch3.value(1)
        else:
            switch3.value(0)
        '''
        sleep(60)

except KeyboardInterrupt:
    pass
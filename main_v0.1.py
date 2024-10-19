import gpiod
import time
from datetime import datetime
# I have 3 Relays one for 5v , another 220v rgb+bulb and last 220v power on/off

# GPIO pin number
pin_number1=17
pin_number2=27
#pin_number3=22

chip=gpiod.Chip('gpiochip4')

switch1=chip.get_line(pin_number1)
switch2=chip.get_line(pin_number2)
#switch3=chip.get_line(pin_number3)

switch1.request(consumer="5v_Light",type=gpiod.LINE_REQ_DIR_OUT)
switch2.request(consumer="220v_Light",type=gpiod.LINE_REQ_DIR_OUT)
#switch3.request(consumer="220v_on_off",type=gpiod.LINE_REQ_DIR_OUT)

switch1.set_value(0)
switch2.set_value(0)
#switch3.set_value(0)

#time for 220v power on/off
on_time_p=datetime.strptime("17:00:00","%H:%M:%S").time()
off_time_q=datetime.strptime("23:00:00","%H:%M:%S").time()

# time for 5v led
on_time_m=datetime.strptime("07:00:00","%H:%M:%S").time()
off_time_m=datetime.strptime("9:00:00","%H:%M:%S").time()
on_time_n=datetime.strptime("17:30:00","%H:%M:%S").time()
off_time_n=datetime.strptime("19:00:00","%H:%M:%S").time()

# time for 220v bulb
on_time_1=datetime.strptime("18:00:00","%H:%M:%S").time()
off_time_2=datetime.strptime("20:45:00","%H:%M:%S").time()
on_time_3=datetime.strptime("21:15:00","%H:%M:%S").time()
off_time_4=datetime.strptime("22:15:00","%H:%M:%S").time()

try:
    while True:
        current_time=datetime.now().time()
        ##### For 5V Temple LED (morning) #####
        #Turn on the relay if the current time is between on_time and off_time
        if (on_time_m<=current_time<=off_time_m) or (on_time_n<=current_time<=off_time_n):
            switch1.set_value(1)
        else:
            switch1.set_value(0)
        time.sleep(60)

        ##### For 220V Study Bulb #####
        if (on_time_1<=current_time<=off_time_2) or (on_time_3<=current_time<=off_time_4):
            switch2.set_value(1)
        else:
            switch2.set_value(0)
        time.sleep(60)

        ##### For 220V Power Switch #####
        '''if on_time_p<=current_time<=off_time_q:
            switch3.set_value(1)
        else:
            switch3.set_value(0)
        '''
except KeyboardInterrupt:
    pass
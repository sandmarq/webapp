import time

import pithing


# Create the pi thing.
pi_thing = pithing.PiThing()


# Now loop forever blinking the LED.
print('Looping with LED blinking (Ctrl-C to quit)...')
while True:
    # Print the current switch state.
    switch = pi_thing.read_switch()
    print('Switch status: {0}'.format(switch))
    pi_thing.set_led(True)
    time.sleep(1)
    pi_thing.set_led(False)
    time.sleep(1)



## PS4 Controller Object. It return a dictionary with multikey support.


Tested on Windows 10. PS4 Controller paired via Bluetooth


Sample Code

import ps4controller
joystick=ps4controller()
joystick.debug=True  # Enable Debug
    while True :
        joystick.read_event()
        time.sleep(0.1)
    pass



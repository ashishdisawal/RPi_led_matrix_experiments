#!/usr/bin/env python

import max7219.led as led
import time
from max7219.font import proportional, CP437_FONT

device = led.matrix(cascaded=1)
device.clear()
device.flush()
time.sleep(1)

try:
  device.show_message("H", font=proportional(CP437_FONT))
  time.sleep(1)
except KeyboardInterrupt:
  # reset array
  device.clear()
  device.flush()
device.clear()
device.flush()



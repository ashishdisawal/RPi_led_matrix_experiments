#!/usr/bin/env python

import max7219.led as led
import time

device = led.matrix(cascaded=1)
device.clear()
try:
  for i in range(8):
    for j in range(8):
      device.pixel(j, i, 1)
      time.sleep(0.1)
      device.pixel(j, i, 0)
except (KeyboardInterrupt, SystemExit):
  # reset array
  device.clear()
  device.flush()
device.clear()
device.flush()



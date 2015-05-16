#!/usr/bin/python
# Single 5x7 LED Matrix with 12 GPIO pins connected to 12 pins on LED Matrix
# Ashish Disawal
# Inspired by http://ezzep.blogspot.in/2012/12/RaspberryPi-5x7LED.html

#include GPIO and Timer Library 
import RPi.GPIO as GPIO
import time

LATCH = 11
CLK = 12
dataBit = 7

sleeptime = 0.25
COLS=range(14,19)


def pulseCLK():
	GPIO.output(CLK, 1)
	time.sleep(sleeptime)
	GPIO.output(CLK, 0)
	return

def serLatch():
	GPIO.output(LATCH, 1)
	time.sleep(sleeptime)
	GPIO.output(LATCH, 0)
	return

def clear():
	for i in COLS:
		GPIO.output(i, GPIO.LOW)

def ssrWrite(value):
	for x in range(0, 1):
		temp = value & 0x80
		print "----> andded temp ", temp
		print "----> x ", x
		if temp == 0x80:
			GPIO.output(dataBit, 1)
		else:
			GPIO.output(dataBit, 0)
		for i in COLS:
			print "--------> COL ", i, "High\n"
			GPIO.output(i, GPIO.HIGH)
	#		raw_input('--> ')
			time.sleep(sleeptime)
			GPIO.output(i, GPIO.LOW)
		print "----> Pluse Clock ", x
		pulseCLK()
		value = value << 0x01
	print "--> Reset Latch"
	serLatch()
	return value

if __name__ == "__main__":
	GPIO.setmode( GPIO.BCM )
	GPIO.setwarnings(False)

	GPIO.setup(LATCH, GPIO.OUT)
	GPIO.setup(CLK, GPIO.OUT)
	GPIO.setup(dataBit, GPIO.OUT)
	
	GPIO.output(LATCH, GPIO.LOW)
	GPIO.output(CLK, GPIO.LOW)
	
	for i in COLS:
		GPIO.setup(i, GPIO.OUT)
		GPIO.output(i, GPIO.LOW)
	
	sr_clock = 1
	for j in range(0,8):
		
		print "\n\t\t----------- %d ---------------- " % j
		print "original sr_clock ", sr_clock
		func_return = ssrWrite(sr_clock)
		print "value ", func_return
		sr_clock = sr_clock << 1
		print "left shift sr_clock ", sr_clock
		time.sleep(sleeptime)
	
#	sr_clock = sr_clock >> 1
#	print "right shift sr_clock ", sr_clock
#	func_return = ssrWrite(sr_clock)
#	print "value ", func_return
#	time.sleep(sleeptime)
	print "Clearing Out\n"
	clear()


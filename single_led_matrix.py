#!/usr/bin/python
# Single 5x7 LED Matrix with 12 GPIO pins connected to 12 pins on LED Matrix
# Ashish Disawal
# Inspired by http://ezzep.blogspot.in/2012/12/RaspberryPi-5x7LED.html

#include GPIO and Timer Library 
import RPi.GPIO as GPIO
import time

class led57_object(object):
	def __init__(self):
		#define Raspberry Pi GPIO number
		self.sleeptime=0.5
		self.COLS=range(14,19)
		self.ROWS=range(2,9)

		#Raspberry Pi GPIO initalization
		GPIO.setmode( GPIO.BCM )
		for i in self.COLS:
			GPIO.setup(i, GPIO.OUT)
		for i in self.ROWS:
			GPIO.setup(i, GPIO.OUT)

	def clear(self):
	#set all GPIO output to LOW
		for i in self.COLS:
			GPIO.output(i, GPIO.LOW)
		for i in self.ROWS:
			GPIO.output(i, GPIO.LOW)

	def demo(self):
		self.clear()
		for j in self.ROWS:
			GPIO.output(j, GPIO.HIGH)
			for i in self.COLS:
				GPIO.output(i, GPIO.HIGH)
				time.sleep(self.sleeptime)
				GPIO.output(i, GPIO.LOW)
			GPIO.output(j, GPIO.LOW)
		self.clear()


def main():
	ledobj=led57_object()
	ledobj.demo()

if __name__ == "__main__":
	main()


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

sleeptime = 0.005
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
	for x in range(0, 8):
		temp = value & 0x80
		if temp == 0x80:
			GPIO.output(dataBit, 1)
		else:
			GPIO.output(dataBit, 0)
		for i in COLS:
			GPIO.output(i, GPIO.HIGH)
			time.sleep(sleeptime)
			GPIO.output(i, GPIO.LOW)
		pulseCLK()
		value = value << 0x01
	serLatch()
	return value

if __name__ == "__main__":
	GPIO.setmode( GPIO.BCM )
	GPIO.setup(LATCH, GPIO.OUT)
	GPIO.setup(CLK, GPIO.OUT)
	GPIO.setup(dataBit, GPIO.OUT)
	
	GPIO.output(LATCH, GPIO.LOW)
	GPIO.output(CLK, GPIO.LOW)
	
	for i in COLS:
		GPIO.setup(i, GPIO.OUT)
		GPIO.output(i, GPIO.LOW)
	
	count = 0
	while count < 8:
		temp = 1
		for j in range(0,8):
			print ssrWrite(temp)
			temp = temp << 1
			time.sleep(sleeptime)
	
		for j in range(0,8):
			temp = temp >> 1
			print ssrWrite(temp)
			time.sleep(sleeptime)
		count += 1
	clear()



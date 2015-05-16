#!/usr/bin/python
# Single 5x7 LED Matrix with one 8-bit shift register, 7 rows connected to shift register
# 5 colomns connected to RPi. 
# Ashish Disawal
# Sat May 16 10:57:24 UTC 2015

#include GPIO and Timer Library 
import RPi.GPIO as GPIO
import time

LATCH = 11
CLK = 12
dataBit = 7
storage_clear = 21

sleeptime = 0.0005
COLS=range(14,19)

A = [[1,1,0,0,0,0,0,1],
     [1,0,1,0,1,1,1,1],
     [0,1,1,0,1,1,1,1],
     [1,0,1,0,1,1,1,1],
     [1,1,0,0,0,0,0,1]]

def pulseCLK():
	GPIO.output(CLK, 1)
#	time.sleep(sleeptime)
	GPIO.output(CLK, 0)
	return

def serLatch():
	GPIO.output(LATCH, 1)
#	time.sleep(sleeptime)
	GPIO.output(LATCH, 0)
	return

def clear():
	for i in COLS:
		GPIO.output(i, GPIO.LOW)
	GPIO.output(storage_clear, GPIO.LOW)

if __name__ == "__main__":
	GPIO.setmode( GPIO.BCM )
	GPIO.setwarnings(False)

	GPIO.setup(LATCH, GPIO.OUT)
	GPIO.setup(CLK, GPIO.OUT)
	GPIO.setup(dataBit, GPIO.OUT)
	GPIO.setup(storage_clear, GPIO.OUT)
	
	GPIO.output(storage_clear, GPIO.HIGH)
	GPIO.output(LATCH, GPIO.LOW)
	GPIO.output(CLK, GPIO.LOW)
	
	for i in COLS:
		GPIO.setup(i, GPIO.OUT)
		GPIO.output(i, GPIO.LOW)
	
	for c in range(2000):
		count = 0
		for i in A:
			if c == 0:
				i.reverse()
			GPIO.output(storage_clear, GPIO.HIGH)
			for j in i:
				GPIO.output(dataBit, j)
				pulseCLK()
			serLatch()
			GPIO.output(COLS[count], GPIO.HIGH)
			time.sleep(sleeptime)
			GPIO.output(COLS[count], GPIO.LOW)
			GPIO.output(storage_clear, GPIO.LOW)
			count += 1

	clear()


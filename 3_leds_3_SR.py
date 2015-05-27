#!/usr/bin/python
# Single 5x7 LED Matrix with one 8-bit shift register, 7 rows connected to shift register
# 5 colomns connected to RPi. 
# Ashish Disawal
# Sat May 16 10:57:24 UTC 2015

#include GPIO and Timer Library 
import RPi.GPIO as GPIO
import time

ROWS = [4, 17, 27, 22, 5, 6, 13]

col_data_1 = 14
col_latch_1 = 15
col_clock_1 = 18

col_latch_2 = 23
col_clock_2 = 24

all_reset = 21

sleeptime = 0.05
small_time = 0.005


def pulse_col_clock_1():
	GPIO.output(col_clock_1, 1)
	time.sleep(small_time)
	GPIO.output(col_clock_1, 0)
	return

def set_col_latch_1():
	GPIO.output(col_latch_1, 1)
	time.sleep(small_time)
	GPIO.output(col_latch_1, 0)
	return

def pulse_col_clock_2():
	GPIO.output(col_clock_2, 1)
	time.sleep(small_time)
	GPIO.output(col_clock_2, 0)
	return

def set_col_latch_2():
	GPIO.output(col_latch_2, 1)
	time.sleep(small_time)
	GPIO.output(col_latch_2, 0)
	return

#def clear():

if __name__ == "__main__":
	GPIO.setmode( GPIO.BCM )
	GPIO.setwarnings(False)

	for row in ROWS:
		GPIO.setup(row, GPIO.OUT)
		GPIO.output(row, GPIO.LOW)
	GPIO.setup(col_latch_1, GPIO.OUT)
	GPIO.setup(col_clock_1, GPIO.OUT)
	GPIO.setup(col_latch_2, GPIO.OUT)
	GPIO.setup(col_clock_2, GPIO.OUT)

	GPIO.output(col_latch_1, GPIO.LOW)
	GPIO.output(col_clock_1, GPIO.LOW)
	GPIO.output(col_latch_2, GPIO.LOW)
	GPIO.output(col_clock_2, GPIO.LOW)

	GPIO.setup(col_data_1, GPIO.OUT)
	GPIO.setup(all_reset, GPIO.OUT)
	GPIO.output(all_reset, GPIO.HIGH)

	A = [[1,1,1,0,0,0,0,0,0,0,0,0,0,1,0,0]]
	for i in range(8):
		print "Iter", i
		GPIO.output(all_reset, GPIO.HIGH)
		for j in A[0]:
			GPIO.output(col_data_1, j)
			pulse_col_clock_1()
			pulse_col_clock_2()
		set_col_latch_1()
		set_col_latch_2()
		for row in ROWS:
			GPIO.output(row, GPIO.HIGH)
			time.sleep(sleeptime)
			GPIO.output(row, GPIO.LOW)
		GPIO.output(all_reset, GPIO.LOW)

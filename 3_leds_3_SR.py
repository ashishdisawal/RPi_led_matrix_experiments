#!/usr/bin/python
# Single 5x7 LED Matrix with one 8-bit shift register, 7 rows connected to shift register
# 5 colomns connected to RPi. 
# Ashish Disawal
# Sat May 16 10:57:24 UTC 2015

#include GPIO and Timer Library 
import RPi.GPIO as GPIO
import time

row_data = 17
row_latch = 27
row_clock = 4

col_data_1 = 14
col_latch_1 = 15
col_clock_1 = 18

col_latch_2 = 23
col_clock_2 = 24

all_reset = 21

sleeptime = 0.05
small_time = 0.05


def pulse_row_clock():
	GPIO.output(row_clock, 1)
	time.sleep(small_time)
	GPIO.output(row_clock, 0)
	return

def set_row_latch():
	GPIO.output(row_latch, 1)
	time.sleep(small_time)
	GPIO.output(row_latch, 0)
	return

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

#TODO def clear() to clear all states
def clear():
	GPIO.output(all_reset, GPIO.LOW)
	set_row_latch()
	set_col_latch_1()
	set_col_latch_2()
#	for i in range(0,8):
#		GPIO.output(row_data, 0)
#		pulse_row_clock()
#	set_row_latch()
#
#	for i in range(0,8):
#		GPIO.output(col_data_1, 0)
#		pulse_col_clock_1()
#	set_col_latch_1()
#
#	for i in range(0,8):
#		pulse_col_clock_2()
#	set_col_latch_2()

if __name__ == "__main__":
	GPIO.setmode( GPIO.BCM )
	GPIO.setwarnings(False)

	GPIO.setup(row_latch, GPIO.OUT)
	GPIO.setup(row_clock, GPIO.OUT)
	GPIO.setup(col_latch_1, GPIO.OUT)
	GPIO.setup(col_clock_1, GPIO.OUT)
	GPIO.setup(col_latch_2, GPIO.OUT)
	GPIO.setup(col_clock_2, GPIO.OUT)

	GPIO.output(row_latch, GPIO.LOW)
	GPIO.output(row_clock, GPIO.LOW)
	GPIO.output(col_latch_1, GPIO.LOW)
	GPIO.output(col_clock_1, GPIO.LOW)
	GPIO.output(col_latch_2, GPIO.LOW)
	GPIO.output(col_clock_2, GPIO.LOW)

	GPIO.setup(row_data, GPIO.OUT)
	GPIO.setup(col_data_1, GPIO.OUT)
	GPIO.setup(all_reset, GPIO.OUT)
	GPIO.output(all_reset, GPIO.HIGH)


	A = [[1,1,1,0,1,0,0,0]]
	print "col_data_1 is 1" 
	GPIO.output(col_data_1, 1)
	for i in range(8):
		print "--> i: ", i
		for j in A[0]:
			print "----> j: ", j
			GPIO.output(row_data, j)
			print "----> pulse_row_clock"
			pulse_row_clock()
		print "--> set_row_latch"
		set_row_latch()
		print "--> pulse_col_clock_1"
		pulse_col_clock_1()
		print "--> set_col_latch_1"
		set_col_latch_1()
		print "--> set col_data_1: 1"
		GPIO.output(col_data_1, 1)
		time.sleep(sleeptime)
		print "----------------------------------"
		s = raw_input("range loop")

	clear()

	

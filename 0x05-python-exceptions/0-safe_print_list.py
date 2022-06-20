#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
	try:
		return [0:x]
	except IndexError:
		print("Index out of range error")


#!/bin/env python2.7
# -*- coding: utf-8 -*-
# detect.py
# Author:   Adrian Marin Portillo
# Date:     August 19th 2015
# Version:  1.1
# Location: https://github.com/mangu93
# Non Windows part is experimental.
# Upgraded variables numbers
import sys
import os
import io
import ctypes
import locale
import re
import subprocess
import platform
if "Windows" in platform.system():
	netsh=subprocess.Popen("netsh wlan show network mode=bssid > list_ssid.txt", shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
	output, errors =  netsh.communicate()
	if errors: 
		print "WARNING: ", errors
		sys.exit(errors)
else:
	netsh=subprocess.Popen("sudo iwlist wlan0 scan", shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
	output, errors =  netsh.communicate()
	if errors: 
		print "WARNING: ", errors
		sys.exit(errors)
pathname = os.path.dirname(sys.argv[0])
file_path = os.path.abspath(pathname)
if "Windows" in platform.system(): 
	txt_path= file_path+"\\list_ssid.txt"
else:
	txt_path= file_path+"/list_ssid.txt"
wifi_list=[0] * 14
with io.open(txt_path) as list_ssid:
	CARRIS_REGEX=r'((Channel+)|(Canal+)){1}(\s)*(:){1}(\s){1}[0-9]{1,2}'
	pattern = re.compile(CARRIS_REGEX)
	for match in pattern.finditer(list_ssid.read()):
		actual_line=match.group(0)
		result=[int(s) for s in actual_line.split() if s.isdigit()]
		for a in result:
			wifi_list[a]=wifi_list[a]+1


if "es_ES" in locale.getdefaultlocale():
	print "RESULTADOS"
	for a in range(0,13):
		real_index=str(a+1)
		num_times=str(wifi_list[a])
		print "Canal "+real_index+" : "+num_times+" ocurrencias."
	print "Recuerda al escoger: cada router ocupa una banda mas las 3 a cada lado."
	raw_input("Pulse una tecla para salir...")
else:
	print "RESULTS"
	for a in range(0,13):
		real_index=str(a+1)
		num_times=str(wifi_list[a])
		print "Channel "+real_index+" : "+num_times+" times."
	print "Remember: pick the channel wisely."
	raw_input("Input something")
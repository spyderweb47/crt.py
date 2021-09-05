#!/usr/bin/env python3

import sys
import requests
import subprocess
import argparse

def get_args():
	parser = argparse.ArgumentParser("crt.py -t <organizarion name or domain> , crt.py will fetch target data from crt.sh and print in json format\ntip:use with tomnomnom tool 'gron'\nAlso you can use put Organization name in target value \n")
	parser.add_argument('-t','--target',dest='target',help="name of target",default="False")
	
	args = parser.parse_args()
	return args


def request(link):
	command =f"https://crt.sh/?q={target}&output=json"
	r = requests.get(command)
	data = r.text
	return data



options = get_args()
target = options.target

if (options.target != "False"):
	target=target.replace(" ","+")
	data=request(target)
	print(data)
else:
	print("specify target")









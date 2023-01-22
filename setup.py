import os
import time
import socket
import subprocess
import requests
import argparse
import readline

parse = argparse.ArgumentParser()
parse.add_argument("-sC", "--scan", help="SCAN_MODE")
parse.add_argument("-t", "--target", help="TARGET")
parse.add_argument("-d", "--delay", help="DELAY", type=float)

args = parse.parse_args()

def scan_port():
	try:
		for port in range(10000):
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			val = sock.connect_ex((args.target, port))
			time.sleep(args.delay)
			if(val==0):
				print("port ---> {} status:open".format(port))
			else:
				pass
		print("Iscanner finalizado 10,000 puertos escaneados")
	except OSError as error:
		print(error)

def gethost(direccion):
	try:
		more = socket.gethostbyaddr(direccion)
		print("namehost: ", more[0])
	except OSError as error:
		print(error)
def funtion_call_ping():
	try:
		subprocess.run(["bash", "./scripts/script.sh", "{}".format(args.target)])
	except OSError as error:
		print(error)

def funtion_get_mac():
	try:
		subprocess.run(["bash", "./scripts/getmac.sh", f"{args.target}"])
	except OSError as error:
		print(error)

def funtion_get_banner():
	try:
		subprocess.run(["cat", "./banner/banner.txt"])
	except OSError as error:
		print(error)
def ident_ttl():
	try:
		file = open("./txt.txt", "r")
		more = file.readlines()
		for x in more:
			crack = x.strip()
			if(crack=="ttl=64" or "ttl==65"):
				print("[+] Sistema operativo unix")
			elif(crack=="ttl=125"):
				print("[+] Sistema operativo Windows")
			else:
				pass
		subprocess.run(["rm", "-rf", "./txt.txt"])
	except OSError as error:
		print(error)
def server_status():
	res = requests.get("http://"+args.target)
	print("response: ", res.status_code)
	if(res.status_code==200):
		print("[*] Posible servidor http activo")
if(args.scan):
	if(args.scan=="bC"):
		if(args.target):
			funtion_get_banner()
			gethost(args.target)
			funtion_call_ping()
			funtion_get_mac()
			server_status()
			ident_ttl()
			scan_port()
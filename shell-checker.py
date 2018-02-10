#!/usr/bin/env python

import argparse, sys, ssl
import requests, urllib2
from threading import Thread
from datetime import datetime
from time import sleep

halah = argparse.ArgumentParser(description="Shell Checker")
halah.add_argument("-l", type=str, action="store", help="List Shell Path")
halah.add_argument("-o", type=str, action="store", help="Output file name")

zeeb = halah.parse_args()

ssl._create_default_https_context = ssl._create_unverified_context
user_agent = {'User-agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'}

class werno:
	rampung='\033[0m'
	ireng='\033[1;30m'
	abang='\033[1;31m'
	ijo='\033[1;32m'
	kuning='\033[1;33m'
	biru='\033[1;34m'
	ungu='\033[1;35m' 
	nila='\033[1;36m'
	putih='\033[1;37m'

def author():
	print '''%s        _____ __         ____      ________              __            
       / ___// /_  ___  / / /     / ____/ /_  ___  _____/ /_____  _____
       \__ \/ __ \/ _ \/ / /_____/ /   / __ \/ _ \/ ___/ //_/ _ \/ ___/
      ___/ / / / /  __/ / /_____/ /___/ / / /  __/ /__/ ,< /  __/ /    
     /____/_/ /_/\___/_/_/      \____/_/ /_/\___/\___/_/|_|\___/_/                 
%s
[+] Usage	: python shell-checker.py -l list.txt -o output.txt	[+] 
	
[+] Author	: Bayu Fedra						[+]
[+] Facebook	: Bayu Fedra  || Instagram : bayufedraa			[+]
[+] Github	: https://github.com/B3yeZ/				[+]
[+] Thanks 	: IndoXploit - Backbox Indonesia - Reversing.ID 	[+]%s''' %(werno.ijo, werno.putih, werno.rampung)

if zeeb.l and zeeb.o:
	try:
		f = open(zeeb.l, "r").read().split()
		w = open(zeeb.o, "w")
		found = []
		forbidden = []
		
		def status():
			if check == 200:
				print werno.ijo +"%s[+] [%s] %s => 200 OK => Shell Found %s" %(werno.ijo, datetime.now().strftime('%H:%M:%S'), x, werno.rampung)
				found.append(x)
			elif check == 300:
				print "[+] [%s] %s => 300 Multiple Choices " %(datetime.now().strftime('%H:%M:%S'), x)
			elif check == 301:
				print "[+] [%s] %s => 301 Moved Permanently " %(datetime.now().strftime('%H:%M:%S'), x)
			elif check == 302:
				print "[+] [%s] %s => 302 Found " %(datetime.now().strftime('%H:%M:%S'), x)
			elif check == 400:
				print "[+] [%s] %s => 400 Bad request " %(datetime.now().strftime('%H:%M:%S'), x)
			elif check == 401:
				print "[+] [%s] %s => 401 Unauthorized " %(datetime.now().strftime('%H:%M:%S'), x)
			elif check == 402:
				print "[+] [%s] %s => 402 PaymentRequired " %(datetime.now().strftime('%H:%M:%S'), x)
			elif check == 403:
				print "%s[+] [%s] %s => 403 Forbidden => Maybe there is a shell %s" %(werno.kuning, datetime.now().strftime('%H:%M:%S'), x, werno.rampung)
				forbidden.append(x)
			elif check == 404:
				print "[+] [%s] %s => 404 Not Found " %(datetime.now().strftime('%H:%M:%S'), x)
			elif check == 500:
				print "[+] [%s] %s => 500 Internal Error " %(datetime.now().strftime('%H:%M:%S'), x)
			elif check == 501:
				print "[+] [%s] %s => 501 Not implemented " %(datetime.now().strftime('%H:%M:%S'), x)
			elif check == 502:
				print "[+] [%s] %s => 502 Service temporarily overloaded " %(datetime.now().strftime('%H:%M:%S'), x)
			elif check == 503:
				print "[+] [%s] %s => 503 Gateway timeout " %(datetime.now().strftime('%H:%M:%S'), x)
			else:
				print "[+] [%s] %s => %d => Respond not idenfified " %(datetime.now().strftime('%H:%M:%S'), x, check)
		
		for x in f:
			if "http://" not in x:
				x = "http://"+x
				
			if "https://" in x:
				x = x.replace("https://", "www.")
				
			try:
				wibu = requests.get(x, headers = user_agent)
				check = wibu.status_code
				status()
					
			except requests.exceptions.ConnectionError:
				try:
					try:
						response = urllib2.urlopen(x)
						print '[+] response headers: "%s"' % response.info()
						
					except IOError, e:
						if hasattr(e, 'code'): 
							print '[+] http error code: ', e.code
						elif hasattr(e, 'reason'): 
							print "[+] can't connect, reason: ", e.reason
						else:
							raise
				except urllib2.URLError, x:
					print "[-] Connection Error! "
				
		print ""
		w.write("[+] Found \n")
		for i in found:
			w.write(i + "\n")
			print "[+] Found => %s" %i
		
		print ""
		w.write("\n\n")
		w.write("[+] Forbidden \n")
		for i in forbidden:
			w.write(i + "\n")
			print "[+] Forbidden => %s" %i
			
		w.close()

	except KeyboardInterrupt:
		w.write("[+] Found \n")
		for i in found:
			w.write(i + "\n")
		
		w.write("\n\n")
		w.write("[+] Forbidden \n")
		for i in forbidden:
			w.write(i + "\n")
			
		w.close()
		
		print ""
		print "[+] Exiting the Program..."
		sys.exit(0)
	
else:
	print werno.abang + "[-] Wrong command! "
	author()
	print werno.kuning
	bener = "Please write the correct command like usage...\n"
	nganggo = "Usage : python shell-checker.py -l file_name.txt -o output_name.txt"
	tampung = ""
	tampung2 = ""
	
	for i in bener:
		tampung += i
		sys.stdout.write("\r[+] %s" %tampung)
		sys.stdout.flush()
		sleep(0.04)
	
	for i in nganggo:
		tampung2 += i
		sys.stdout.write("\r[+] %s" %tampung2)
		sys.stdout.flush()
		sleep(0.04)
		
	print werno.rampung
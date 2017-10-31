#!/usr/bin/python
# -*- coding: UTF-8 -*-
#COded By Badreddine CHamkhi ;)
#Mon 23:08
#Shareout To all fallaga Team Tunisian Cyber resistance
#Don't CHange My rights Please ;)
		#Import Zone
from urllib2 import Request, urlopen, URLError, HTTPError
import os
from platform import system
import sys
##########################################
#########ClearScreen######################
##########################################
def clear():
	if system() == 'Linux':
		os.system('clear')	
	if system() == 'Windows':
		os.system('cls')
clear()
##########################################
#############Banner######################
##########################################
banner = ''' \033[1;36m
           ____                      ,
          /---.'.__             ____//
               '--.\           /.---'
          _______  \\         //
        /.------.\  \|      .'/  ______
       //  ___  \ \ ||/|\  //  _/_----.\__
      |/  /.-.\  \ \:|< >|// _/.'..\   '--'
         //   \'. | \'.|.'/ /_/ /  \\
        //     \ \_\/" ' ~\-'.-'    \\
       //       '-._| :H: |'-.__     \\
      //           {/'==='\}'-._\     ||
      ||                        \\    \|
      ||                         \\    '
      |/                          \\
                                   ||
                                   ||
                                   \\
                                    '                      
\033[1;m
'''
author = '''
    \033[1;42m[ AdminPanel Grabber v 1.0 ]\033[1;m
    \033[1;42m[ Coded By Badreddine Chamkhi ]\033[1;m
'''
print banner
print author
##########################################
##########RealWOrk########################
##########################################
def findAdmin():
	f = open("admin.txt","r");
	link = raw_input("\033[1;41mEnter Site Name Please :\033[1;m")
	print "\033[1;44mResults Will Be Shown Here :\033[1;m"
	while True:
		sub_link = f.readline()
		if not sub_link:
			break
		req_link = "http://"+link+"/"+sub_link
		req = Request(req_link)
		try:
			response = urlopen(req)
		except HTTPError as e:
			continue
		except URLError as e:
			continue
		else:
			print "\033[1;43m[+] Found In :\033[1;m ",req_link
findAdmin()
print "\033[1;41m[+] Job Completed ! Exiting :D\033[1;m"
#COntact : bchemkh.1919@gmail.com




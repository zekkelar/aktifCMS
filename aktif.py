import urllib3, requests, os, sys, re, json
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import base64
import random
import string
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
from multiprocessing.dummy import Pool as ThreadPool
from time import time as timer
from platform import system	
from colorama import Fore								
from colorama import Style								
from pprint import pprint								
from colorama import init
import urllib
fr  =   Fore.RED											
fc  =   Fore.CYAN											
fw  =   Fore.WHITE											
fg  =   Fore.GREEN											
sd  =   Style.DIM											
sn  =   Style.NORMAL										
sb  =   Style.BRIGHT
try:
	ganteng = input('ur files => ')
	f= open(ganteng, 'r') 
	woh = f.read().splitlines()
except IOError:
	pass
woh = list((woh))

def banner():
	sd 
	print ("""
		[ = ] AKTIF CMS BY Zekkel AR [ = ]
		[ = ] Family Attack Cyber    [ = ]
""")
def Domains(url):

	if '://' not in url:
		return "http://" + url
	else:
		return url

def aktif(site):
	url = Domains(site)
	exploit = ['/aktifcms/upload/docs1.php', '/aktifcms/upload/docs.php', '/aktifcms/upload/resim.php ']
	for za in exploit:
		bece = url+za
		l = requests.get(bece)
		if l.status_code == 200:
			print('[ {}VULN ] {}{}' .format(fc,fg,bece))
		else:
			print('[ {}NOT VULN ] {}{}' .format(fr,fg,bece))
def Run_Work(site):
	url = Domains(site)
	aktif(url)

os.system('clear')
banner()
def Main():


	start = timer()
	pp = ThreadPool(40)
	pr = pp.map(Run_Work, woh)
	print('Time: ' + str(timer() - start) + ' seconds')


if __name__ == "__main__":
	Main()

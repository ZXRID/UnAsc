######################################
#           Made by ZXRID            #
#     Follow Instagram: @zurstx_     #
######################################
import os, sys, string, time, platform, base64
if platform.python_version().split('.')[0] != '2':
	masukkk = input
	type = 'py3'
	sym = base64.b16decode(b'E280A2')
else:
	masukkk = raw_input
	type = 'py2'
	sym = '\xe2\x80\xa2'

ngentot = '   __  __      ___              _ _\n  / / / /___  /   |  __________(_|_)\n / / / / __ \\/ /| | / ___/ ___/ / /\n/ /_/ / / / / ___ |(__  ) /__/ / /\n\\____/_/ /_/_/  |_/____/\\___/_/_/ Converter\n     By ZXRID ' + sym.decode('utf-8') + ' BlackCoderCrush\n        Python Version: ' + type
def zxrid(text):
	for percent in range (1,101):
		sys.stdout.write("\r" + text + " [" + str(percent) + "%]")
		sys.stdout.flush()
		time.sleep(00.01)
def main():
	os.system('clear')
	print(ngentot)
	print("[01] Convert now\n[02] About\n[00] Exit\n[==]")
	ch1 = masukkk("[Choose]> ")
	if ch1 == "":
		exit("Dont empty")
	elif ch1 in ('01','1'):
		convert()
	elif ch1 in ('02','2'):
		about()
	elif ch1 in ('00','0'):
		exit("Exited.")
	else:
		exit("Check your input")
def convert():
	files = masukkk("Input Logo File: ")
	try:
		set = open(files,'r').read()
	except IOError:
		exit("File not found!")
	time.sleep(1.5)
	zxrid("Converting")
	resu = repr(set).replace('\\\\','\\')
	try:
		date = time.strftime('%H:%M %d-%m-%Y')
		saving = open('unascii_result.txt','a')
		saving.write(date + '\nFrom : ' + str(files) + '\nType : ' + type + '\n' + resu + '\n' + 150 * '#' + '\n')
		saving.close()
		print("\nSuccess! Output : unascii_result.txt")
	except:
		print("Error!")
def about():
	os.system('clear')
	print(ngentot.center(55))
	print('             Tool Name : UnAscii Converter\n                Author : ZXRID\n                  Date : 4 Des 2019\n                  Team : Black Coder Crush\n               Version : end/' + type)
	masukkk('\n\n\nEnter to back')
	main()
try:
	main()
except KeyboardInterrupt:
	exit("Interrupted")

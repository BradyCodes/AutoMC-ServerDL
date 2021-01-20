import os
import time
import sys

server_jar_link = 'https://launcher.mojang.com/v1/objects/1b557e7b033b583cd9f66746b7a9ab1ec1673ced/server.jar'

class Linuxsys:
    def __init__(self, link, systype):
        self.link = link
        self.sys = systype
    
    def Downloader(self):
        os.system('wget ' + server_jar_link)

    def run(self):
        print('To run a Minecraft server, you must install Java')
        yn = input('Continue: [Y/n]')
        os.system('sudo apt install java')
        time.sleep(1)
        print('Starting')
        os.system('java -Xmx1024M -Xms1024M -jar server.jar nogui ')
class MacOS:
    def __init__(self, link, systype):
        self.link = link
        self.sys = systype
    
    def Downloader(self):
        os.system('curl ' + server_jar_link + ' ' + '--output server.jar')

    def run(self):
        os.system('brew --version')
        print('To run a minecraft server, you must have Java installed')
        yn = input('Continue: [Y/n]')
        os.system('brew install java')
        print('Installed')
        time.sleep(1)
        print('Running')
        os.system('java -Xmx1024M -Xms1024M -jar server.jar nogui ')
class Windows:
    def __init__(self, link, systype):
        self.link = link
        self.sys = systype
    
    def Downloader(self):
        os.system('cmd /k curl ' + server_jar_link + ' ' + '--output server.jar')

    def run(self):
        print('To run a minecraft server, you must have Java installed')
        print('Running')
        time.sleep(1)
        clear()
        print('Running..')
        time.sleep(1)
        os.system('java -Xmx1024M -Xms1024M -jar server.jar nogui ')

def clear():
    os.system('clear')    
def windows():
    clear()
    w = Windows(server_jar_link, 'Windows')
    w.Downloader()
    w.run()
    clear()
    print('Go to EULA.txt and change eula=false to eula=true and run start.py')
def linux():
    clear()
    l = Linuxsys(server_jar_link, 'Linux/Ubuntu')
    l.Downloader()
    l.run()
    clear()
    print('Go to EULA.txt and change eula=false to eula=true and run start.py')
def macos():
    clear()
    m = MacOS(server_jar_link, 'MacOS')
    m.Downloader


clear()
print('1:  Windows ')
print('2:  MacOS ')
print('3:  Linux ')


start = input('Enter your OS: [1, 2, 3] ')


if start == '1':
    windows()
elif start == '2':
    macos()
else:
    linux()
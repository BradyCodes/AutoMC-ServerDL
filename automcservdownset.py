import os
import time
import sys

server_jar_link = 'https://launcher.mojang.com/v1/objects/1b557e7b033b583cd9f66746b7a9ab1ec1673ced/server.jar'

def clear():
    os.system('clear')    

def windows():
    pass
def linux():
    clear()

def macos():
    pass


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


macdown = Linuxsys(server_jar_link, 'Ubuntu')
macdown.Downloader()
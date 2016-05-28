"""
Webserver.py   version 0.01
Реализация веб-сервера, способная запускать серверные CGI-сценарии; обслуживает файлы и сценарии в текущем рабочем каталоге;
сценарии должны находиться webdir\cgi-bin    or webdir\htbin    
"""
import os, sys
from http.server import HTTPServer, CGIHTTPRequestHandler

webdir = '.'  #Место с файлами хтмл и подкаталог cgi-bin
port = 80 # по умолчанию localhost:xxxx

os.chdir(webdir)  # Перейти в корневой каталог ХТМЛ
srvaddr = ("", port)  #Имя хоста и номерпорта
srvobj = HTTPServer(srvaddr, CGIHTTPRequestHandler)
srvjob.serve_forever()

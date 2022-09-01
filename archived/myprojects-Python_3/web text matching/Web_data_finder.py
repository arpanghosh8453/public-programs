
import requests
from bs4 import BeautifulSoup
import os

ask = input("\nEnter the full path of CSV file : ")
url = input("\nEnter the full URL with http:// : ")

try:

  #url = 'https://en.wikipedia.org/wiki/Plague_(disease)'
  res = requests.get(url)
  html_page = res.content
  soup = BeautifulSoup(html_page, 'html.parser')
  text = soup.find_all(text=True)

  output = ''
  blacklist = [
    '[document]',
    'noscript',
    'header',
    'html',
    'meta',
    'head', 
    'input',
    'script',
      'style',
    # there may be more elements you don't want, such as "style", etc.
  ]

  for t in text:
    if t.parent.name not in blacklist:
      output += '{} '.format(t)

except:

  print( '\nError Reading URL : Make sure you give the full valid Url including http:// also')


try:
  ask.replace("\\","/")
  ask = ask[1:]
  ask = ask[:-1]
  print(ask)
  fin = open(ask,'r')
  word_list = map( lambda x : x.lower() , fin.read().split('\n'))
  fin.close()

except:
  print("\nError reading File name : Wrong file path.")

output = output.lower()
result = filter(lambda item : ((" "+item+" " in output) or ("\n"+item+" " in output)) or (" "+item+"\n" in output) , word_list )

final_data = '\n'.join(result)

print("\nMatched Keywords : \n\n"+final_data)

try:
  out = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')+"\\output.csv"
  fout = open(out,'w')
  fout.write(final_data)
  fout.close()
  print('\nData written in : '+out)
except:
  print("\nError saving file : File with same name output.csv already present and Permission denied !")


x = input("\nEnter to Exit : ")
#print(output)
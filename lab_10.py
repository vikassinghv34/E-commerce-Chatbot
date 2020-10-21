"""
import re
name=input('enter any string ')

pattern='^[A-Z].*'
if re.search(pattern,name):
    print('first character of the string is upper case')
else:
    print('First character is not upper case')
"""
"""
import re

date=input('write any date with some text ')
pattern=r'^(.*)\d{2}[-/]\d{2}[-/]\d{4}(.*)'

if re.search(pattern,date):
    print('date is found')
else:
    print('date is missing')
"""
"""
import re
ip=input("enter a ip address ")
pattern='\d{1,3}[.]\d{1,3}[.]\d{1,3}[.]\d{1,3}'
if re.search(pattern,ip):
    print('ip is correct')
else:
    print('ip is incorrect')
"""
"""
import re
url=input('enter valid url ')
pattern=r'^\w{4,5}[:][/]{2}www[.]\w+[.]\w+([?/]\w+)?'
if re.search(pattern,url):
    print('valid url')
else:
    print('invalid url')
"""
""""
import re
anum=input("enter some text with numbers ")
pattern="\w+"
if re.search(pattern,anum):
    print("it is an alpha numeric")
else:
    print('it is not an alpha numeric')
"""
"""
import re
tstring=input('input date in time string')
pattern="^([01]?[0-9]|2[0-3]):[0-5][0-9]"
if re.search(pattern,tstring):
    print('value is in time string format')
else:
    print('value is not in time string format')
"""
"""
import re

hexcolor=input('enter color code ')
pattern="^#[A-Fa-f0-9]{6}|[A-Fa-f0-9]{3}"
if re.search(pattern,hexcolor):
    print("code is valid")
else:
    print('color code is invalid')
"""

import re

url=input('enter a url')
pattern=r"/(\d{4})/(\d{2})/(\d{2})/"
search=re.findall(pattern,url)
if search:
    print(search)
else:
    print("date not found")
import urllib
import urllib2
import requests

a = 1
b = 2
c = 3

strPath =
f = open(strPath)
strText = f.read()

if strText = a
    url = 'insert url here'

    print "downloading with urllib"
    urllib.urlretrieve(url, "insert package name here")

    print "downloading with urllib2"
    f = urllib2.urlopen(url)
    data = f.read()
    with open("code2.zip", "wb") as code:
        code.write(data)

    print "downloading with requests"
    r = requests.get(url)
    with open("code3.zip", "wb") as code:
        code.write(r.content)
        
if strText = b
    url = 'insert url here'

    print "downloading with urllib"
    urllib.urlretrieve(url, "insert package name here")

    print "downloading with urllib2"
    f = urllib2.urlopen(url)
    data = f.read()
    with open("code2.zip", "wb") as code:
        code.write(data)

    print "downloading with requests"
    r = requests.get(url)
    with open("code3.zip", "wb") as code:
        code.write(r.content) 
        
if strText = c
    url = 'insert url here'

    print "downloading with urllib"
    urllib.urlretrieve(url, "insert package name here")

    print "downloading with urllib2"
    f = urllib2.urlopen(url)
    data = f.read()
    with open("code2.zip", "wb") as code:
        code.write(data)

    print "downloading with requests"
    r = requests.get(url)
    with open("code3.zip", "wb") as code:
        code.write(r.content)

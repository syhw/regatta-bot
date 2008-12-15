import cookielib, urllib, urllib2
from bot_commons import *

mail = 'spamygaby@gmail.com'
password = '100886'
pseudo = 'Snippy.CsT'
key = '095f36f60a49d35fe436c667e18ed17c' # pass hash ? static

cookiejar = cookielib.CookieJar()
urlOpener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookiejar))
values = {'mail':mail, 'pass':password, 'button':'Valider'}
data = urllib.urlencode(values)
request_headers = { 'User-Agent': 'Firefox/3.0.4' }
request = urllib2.Request("http://www.virtualregatta.com/login.php", data, request_headers)
url = urlOpener.open(request)
page = url.read(500000)

if not 'PHPSESSID' in [cookie.name for cookie in cookiejar]:
  raise ValueError, "Login failed with login=%s, password=%s" % (mail, password)

if SHOW_ALL:
  print "We are logged in !"
  print '------------------'
  for cookie in cookiejar:
    print cookie.name
    #print cookie
  print '------------------'

import speed # best(angle) returns ('number_of_the_sail', float(speed))
speed.best(127)

request = urllib2.Request("http://vendeeglobe.virtualregatta.com/get_course.php", { }, request_headers)
opener = urllib2.build_opener()
get_course = opener.open(request).read(500000)
values = {'pseudo':pseudo, 'clef':key}
data = urllib.urlencode(values)
request = urllib2.Request("http://vendeeglobe.virtualregatta.com/get_user.php", data, request_headers)
opener = urllib2.build_opener()
get_user = opener.open(request).read(500000)



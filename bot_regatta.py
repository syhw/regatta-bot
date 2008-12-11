import cookielib, urllib, urllib2

mail = 'spamygaby@gmail.com'
password = '100886'
show_all = 1

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
print "We are logged in !"

if show_all:
  for cookie in cookiejar:
    print cookie.name



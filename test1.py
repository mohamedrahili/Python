from urllib import request
url = "http://www.osbt.com"
content = request.urlopen(url).read()
print(content)
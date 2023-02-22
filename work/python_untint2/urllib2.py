import urllib.request
response = urllib.request.urlopen('https://www.amz123.com/usatopkeywords-1-1-.htm?rank=&uprank=')
#print(type(response))
# books = response.read().decode('utf-8')
# print(type(books))
# print(dir(response))
headers = response.getheaders()
print(headers)
#print(books)

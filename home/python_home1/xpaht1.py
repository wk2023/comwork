import requests
from lxml import etree

request = requests.get('https://www.amz123.com/jptopkeywords')
# print(request.text)
html = etree.HTML(request.text)
# result = etree.tostring(html)
# result.decode('utf-8')
result = html.xpath(
    '/html/body/div[3]/main/div[2]/div[1]/div[2]/div[1]/a/text()')
print(result)
result2 = html.xpath('//title/text()')
print(result2)
result3 = html.xpath(
    '/html/body/div[3]/main/div[2]/div[1]/div/div[1]/a/text()')
print(type(result3))
for words in result3:
    print(words)

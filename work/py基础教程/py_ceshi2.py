# 字符串索引造作
#from math import pi
""" words = 'goodnaitet'
print(words[0]) # 字符串可以用索引标识 来显示单独字母
list = [24]*5
print(list) """
# 第三章 3.1
# website = 'http://www.python.org'
#website[-3:] = 'com'  # 非法 字符串元素复制 切片赋值都是非法  切片赋值列表可以
""" print(website[-3:]) # 提取可以 赋值不可以
print('{},{} and {}'.format('first','second','third')) # 替换花括号里面的内容
# first,second and third

a = '{0},{1} and {2}'.format('first','second','third')  #按照花括号里面的数字，提取后期对于位置
# first,second and third
print(a)

a = '{name} is approximately {value:.2f}.'.format(value=pi,name='pai')  #按照字符串
print(a)
a = 'http://wwww.python.{org}'.format(org='com') 
#  http://wwww.python.com
print(a) """
#3.4 字符串的方法
print('the middle by jimmy eat world'.center(39,'*'))  # 以指定宽度字符串，字符串居中，第二个参数是填充符号，默认空格
title= 'monty python'
print(title.find('m'))  # 查找字符串中的字符串，找到返回位置  从0开始，没有找到返回-1
print(title.find('t',1,10)) #后面两个参数表示 开始 和结束位置  包括前面 不包括后面
a = {'d','a','c'}
print(''.join(a)) # 合并列表 形成字符串，序列里面必须全部是字符串，序列作为参数传入，前面代码一什么作为分隔符，‘’就代表空 
b = 'Tromhe In Hammer'
print(b.lower()) # 返回 字符串的小写，但是仅仅返回，实际原版没有变化
print(b)
print('this is a test is'.replace('is','iis'))  # 替换字符串里面 指定字符

a = '1+2+3+4+5'.split('+') # 以#作为分隔符 把字符串拆分为列表，如果用’‘ 则拆分每格字符
print(a)
a = '   the mode  '
print(a.strip())  #去除字符串卡头和结尾的空白
table = str.maketrans('dd','cc','1') #  第一个参数表示 要替换内容，第二次参数表示替换内容  第三次参数表示要删除内容
print('wo dd to 1'.translate(table))  # tanslate 替换字符串中的内容，但是需要传入 maketrans 类型的转换表
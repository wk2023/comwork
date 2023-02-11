# 字符串索引造作
""" words = 'goodnaitet'
print(words[0]) # 字符串可以用索引标识 来显示单独字母
list = [24]*5
print(list) """
# 第三章 3.1
website = 'http://www.python.org'
#website[-3:] = 'com'  # 非法 字符串元素复制 切片赋值都是非法  切片赋值列表可以
print(website[-3:]) # 提取可以 赋值不可以
print('{},{} and {}'.format('first','second','third')) # 替换花括号里面的内容
# first,second and third

a = '{0},{1} and {2}'.format('first','second','third')  #按照花括号里面的数字，提取后期对于位置
# first,second and third
print(a)

a = '{name} is approximately {value:.2f}.'.format(value=pi,name='pai')  #按照字符串
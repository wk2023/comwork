print(r'c:\tttd\\')  
print('c:\ttd\\')  #r 对字符串末尾的\ 不起作用 仍会当成转移字符  需要前面在加个\ 来转义.但是如果前面带 r  后面转义会显示\\。所有用r 不要再字符串末尾用\. 非得用 必须用\。转义。在加上‘’ 单独隔离
print(r'c:\ttd''\\')  # 正确


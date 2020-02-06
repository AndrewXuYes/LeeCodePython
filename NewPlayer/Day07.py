s1 = 'hello, world!'
s2 = "hello, world!"
# 以三个双引号或单引号开头的字符串可以折行
s3 = """
hello, 
world!"""
print(s1, s2, s3)

s1 = '\141\142\143\x61\x62\x63'
s2 = '\u9a86\u660a'
print(s1, s2)
print()

s1 = r'\'hello, world!\''
s2 = r'\n\\hello, world!\\\n'
print(s1, s2)
print()

a, b = 5, 10
print('%d * %d = %d' % (a, b, a * b))
print()

str1 = 'hello, world!'
# 通过内置函数len计算字符串的长度
print(len(str1)) # 13
# 获得字符串首字母大写的拷贝
print(str1.capitalize()) # Hello, world!
# 获得字符串每个单词首字母大写的拷贝
print(str1.title()) # Hello, World!
# 获得字符串变大写后的拷贝
print(str1.upper()) # HELLO, WORLD!
print()

list1 = [1, 3, 5, 7, 100]
print(list1) # [1, 3, 5, 7, 100]
# 乘号表示列表元素的重复
list2 = ['hello'] * 3
print(list2) # ['hello', 'hello', 'hello']
# 计算列表长度(元素个数)
print(len(list1)) # 5
# 下标(索引)运算
print(list1[0]) # 1
print()

f = [x for x in range(1, 5)]
print(f)
f = [x + y for x in 'ABCD' for y in '1234']
print(f)
print()

set1 = {1, 2, 3, 3, 3, 2}
print(set1)
print('Length =', len(set1))
print()


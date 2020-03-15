# -------------------------
# 文件内建函数和方法
    # open() 打开文件
    # read() 输入
    # readline() 输入一行
    # seek() 文件内移动
    # write() 输出
    # close() 关闭文件
# -------------------------

# 写入文件 ------ open() ---> write() ---> close()
# 读取文件 ------ open() ---> read()  ---> close()

# 将小说的主要人物记录在文件中
# file1 = open('name.txt', 'w')
# file1.write('诸葛亮')
# file1.close()

# file2 = open('name.txt')
# print(file2.read())
# file2.close()

# file3 = open('name.txt', 'a')
# file3.write('\n')
# file3.write('刘备')
# file3.close()

# file4 = open('name.txt')
# print(file4.readline())
# file4.close()

# file5 = open('name.txt')
# for line in file5.readlines():
#     print(line)
#     print('------')
# file5.close()

file6 = open('name.txt')
print('当前文件指针的位置是 %s' %file6.tell()) # 查看文件指针的位置
print('当前读取到了一个字符，字符的内容是 %s' % file6.read(1))
print('当前文件指针的位置是 %s' %file6.tell())
# 第一个参数代表偏移的位置，第二个参数 0 表示从文件开头偏移， 1 表示从当前位置偏移， 2 从文件结尾
file6.seek(5, 0) # 表示从开头开始偏移5个位置
print('我们进行了seek的操作')
print('当前文件指针的位置是 %s' %file6.tell())
print('当前读取到了一个字符，字符的内容是 %s' % file6.read(1))
print('当前文件指针的位置是 %s' %file6.tell())
file6.close()










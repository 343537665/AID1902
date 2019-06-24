import pymysql
import re

# 打开文本
f = open("dict.txt")

# 1 建立数据库连接
db = pymysql.connect("localhost", "root", "123456", "dict")

# 2 创建游标对象
cursor = db.cursor()

# 将文本拆分成单词和解释插入dict库中的words表的两个字段中
for line in f:
    l = re.split(r"\s+", line)
    word = l[0]
    interpret = ' '.join(l[1:])

    sql = "insert into words (word,interpret) \
    values('%s','%s')" % (word, interpret)

    try:
        # 3 游标方法
        cursor.execute(sql)
        # 4 提交到数据库
        db.commit()
    except:
        db.rollback()

# #5、关闭游标对象
# cursor.close()
#
# #6、断开数据库连接
# db.close()

f.close()

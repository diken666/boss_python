from pymongo import MongoClient

client = MongoClient('localhost', 27017)
names = client.list_database_names()

# 输出本地所有的数据库名字
print(names)

# 选择其中的local数据库， （local数据库是安装时自带的，项目中我们应该自己新建一个）
db = client.local

# 向local数据库中的startup_log集合中插入一条数据
db.startup_log.insert_one({'testInfo': 789})

# 打印local数据库中start_log集合的所有数据
for i in db.startup_log.find():
    print(i)


from pymongo import MongoClient

# 主机名
host = 'localhost'
# 端口号
port = 27017

# 获取mongo数据库 (数据库名，集合名)
def getMongoDB(dbName, colName):
    client = MongoClient(host, port)
    return client[dbName][colName]


# 向数据库中插入多条数据
def insertManyDataToMongoDB(db, data):
    try:
        db.insert_many(data)
        print("存入数据成功！")
    except BaseException:
        print("存入数据失败！")


# 删除集合中的所有数据
def delAllDataInCol(db):
    try:
        db.delete_many({})
        print("数据删除成功！")
    except BaseException:
        print("数据删除失败！")



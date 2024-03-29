# 引用第三方beautifulSoup库
from bs4 import BeautifulSoup
# 引用python自带的urllib库
import urllib.request
# 引入自定义的mongodb的函数
import mongo_def as mongo

# 数据库的名字
dbName = 'jobInfo'
# 数据库集合的名字
colName = 'testInfo'

# 获取网页的bs对象
def getBsObj(url, headers):
    request = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(request)
    bs_obj = BeautifulSoup(response.read().decode('utf-8'), features="html.parser")
    return bs_obj


# 获取每个公司详细信息
def getCompanyInfo(bsObj):
    res = []
    for item in bsObj.findAll('div', {"class": 'job-primary'}):
        name = getComNameAndLink(item)
        tagInfo = getComTagInfo(item)
        jobInfo = getJobNameAndSalary(item)
        jobTagInfo = getJobTagInfo(item)
        if name and tagInfo and jobInfo and jobTagInfo:
            res.append({
                "comName": name["comName"],
                "comLink": name["comLink"],

                "jobName": jobInfo["jobName"],
                "jobLink": jobInfo["jobLink"],
                "minSalary": jobInfo["minSalary"],
                "maxSalary": jobInfo["maxSalary"],

                "city": jobTagInfo["city"],
                "positionArea": jobTagInfo["positionArea"],
                "positionLoc": jobTagInfo["positionLoc"],
                "expDescription": jobTagInfo["expDescription"],
                "minExp": jobTagInfo["minExp"],
                "maxExp": jobTagInfo["maxExp"],
                "education": jobTagInfo["education"],

                "direction": tagInfo["direction"],
                "finSituation": tagInfo["finSituation"],
                "comSize": tagInfo["comSize"]
            })
    return res

# 获取公司名字和公司链接
def getComNameAndLink(item):
    try:
        comName = item.find('div', {'class': 'info-company'}).div.h3.a.get_text()
        comLink = item.find('div', {'class': 'info-company'}).div.h3.a.get('href')
        return {
            "comName": comName,
            "comLink": comLink
        }
    except BaseException:
        print("comName err->\n", item.find('div', {'class': 'info-company'}))


# 获取公司标签信息
def getComTagInfo(item):
    try:
        # [3: -4]去除p标签符号
        # tagInfo结构类似 ['游戏', '未融资', '20-99人']
        tagInfo = str(item.find('div', {'class': 'info-company'}).div.p)[3:-4].split('<em class="vline"></em>')
        direction = tagInfo[0]
        finSituation = ''
        comSize = tagInfo[-1]
        # 因为有的标签没有融资情况的介绍，所以要对长度=3时进行适配
        if len(tagInfo) == 3:
            finSituation = tagInfo[1]
        return {
            "direction": direction,
            "finSituation": finSituation,
            "comSize": comSize
        }
    except BaseException:
        print('comTagInfo err->\n', item.find('div', {'class': 'info-company'}).div.p)


# 获取招聘职位信息和薪水
def getJobNameAndSalary(item):
    try:
        jobName = item.find('div', {'class': 'info-primary'}).h3.a.div.get_text()
        salaryStr = item.find('div', {'class': 'info-primary'}).h3.a.span.get_text()
        jobLink = item.find('div', {'class': 'info-primary'}).h3.a.get('href')
        # 去除salaryStr后面的“·xx薪”
        salary = salaryStr.split('·')[0][:-1].split('-')
        minSalary = 0
        maxSalary = 0
        if len(salary) == 2:
            minSalary = int(salary[0])
            maxSalary = int(salary[1])
        return {
            "jobName": jobName,
            "minSalary": minSalary,
            "maxSalary": maxSalary,
            "jobLink": jobLink
        }
    except BaseException:
        # 有的公司是采用日结工资的形式，如 200-300/天，暂时对此形式的不予采集
        print('salary err->\n', item.find('div', {'class': 'info-primary'}).h3.a)


# 获取工作的标签信息
def getJobTagInfo(item):
    try:
        tagInfo = str(item.find('div', {'class': 'info-primary'}).p)[3:-4].split('<em class="vline"></em>')
        # tagInfo数据结构如 ['成都 武侯区 新会展', '1-3年', '大专']
        if len(tagInfo) == 3:
            # 所在城市
            city = tagInfo[0].split(' ')[0]
            # tempArr数据结构如 ['成都', '武侯区', '桂溪']
            tempArr = tagInfo[0].split(' ')
            # 具体位置
            location = ''
            # 拼接location地址
            for i in range(1, len(tempArr)):
                if i == 1:
                    location += tempArr[i]
                else:
                    location += ' ' + tempArr[i]
            # 学历要求
            education = tagInfo[2]
            # 工作经验，主要对【1年以内，1-3年，3-5年，5-10年，10年以上】情况做处理，其他情况保留原字段就可以
            expDescription = tagInfo[1]
            minExp = None
            maxExp = None
            if tagInfo[1] == '1年以内':
                minExp = 0
                maxExp = 1
            elif tagInfo[1] == '1-3年':
                minExp = 1
                maxExp = 3
            elif tagInfo[1] == '3-5年':
                minExp = 3
                maxExp = 5
            elif tagInfo[1] == '5-10年':
                minExp = 5
                maxExp = 10
            elif tagInfo[1] == '10年以上':
                minExp = 10
                maxExp = 99
            return {
                "city": city,
                "positionArea": location.split(' ')[0],
                "positionLoc": location.split(' ')[1],
                "education": education,
                "expDescription": expDescription,
                "minExp": minExp,
                "maxExp": maxExp
            }
    except BaseException:
        print('jobTag err->\n', str(item.find('div', {'class': 'info-primary'}).p)[3:-4])


# 保存一页的数据到数据库
def saveDataToMongoDB(res):
    db = mongo.getMongoDB(dbName, colName)
    mongo.insertManyDataToMongoDB(db, res)


# 删除数据库中所有数据
def deleteAllData():
    db = mongo.getMongoDB(dbName, colName)
    mongo.delAllDataInCol(db)

# 引用第三方beautifulSoup库
from bs4 import BeautifulSoup
# 引用python自带的urllib库
import urllib.request


# 获取网页的bs对象
def getBsObj(url, headers):
    request = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(request)
    bs_obj = BeautifulSoup(response.read().decode('utf-8'), features="html.parser")
    return bs_obj


# 获取每个公司详细信息
def getCompanyInfo(bsObj):
    for item in bsObj.findAll('div', {"class": 'job-primary'}):
        name = getComNameAndLink(item)
        print(name)
        tagInfo = getComTagInfo(item)
        print(tagInfo)
        jobInfo = getJobNameAndSalary(item)
        print(jobInfo)


# 获取公司名字和公司链接
def getComNameAndLink(item):
    name = item.find('div', {'class': 'info-company'}).div.h3.a.get_text()
    companyLink = item.find('div', {'class': 'info-company'}).div.h3.a.get('href')
    return [name, companyLink]


# 获取公司标签信息
def getComTagInfo(item):
    # [3: -4]去除p标签符号
    tagInfo = str(item.find('div', {'class': 'info-company'}).div.p)[3:-4].split('<em class="vline"></em>')
    return tagInfo


# 获取招聘职位信息和薪水
def getJobNameAndSalary(item):
    jobName = item.find('div', {'class': 'info-primary'}).h3.a.div.get_text()
    salaryStr = item.find('div', {'class': 'info-primary'}).h3.a.span.get_text()
    # 去除salaryStr后面的“·xx薪”
    salary = salaryStr.split('·')[0][:-1].split('-')
    minSalary = 0
    maxSalary = 0
    if len(salary) == 2:
        minSalary = int(salary[0])
        maxSalary = int(salary[1])
    return [jobName, minSalary, maxSalary]


# 获取工作的标签信息
def getJobTagInfo(item):
    item.find('div', {'class': 'info-primary'}).h3.a.div.get_text()


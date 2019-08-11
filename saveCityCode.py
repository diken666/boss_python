# 引用第三方beautifulSoup库
from bs4 import BeautifulSoup
# 引用python自带的urllib库
import urllib.request
import json

# 目标网站
url = "https://www.zhipin.com/wapi/zpCommon/data/city.json"
# 模拟浏览器的user-agent
UA = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
headers = {
    'User-Agent': UA
}


# 获取网页的bs对象
def getBsObj(url, headers):
    request = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(request)
    bs_obj = BeautifulSoup(response.read().decode('utf-8'), features="html.parser")
    return json.loads(str(bs_obj))


def write_json(jlist):
    # 将bx列表写入json文件
    with open('data/cityCode.json', 'w') as f_obj:
        json.dump(jlist, f_obj)


res = getBsObj(url, headers)
result = []
cityList = res['zpData']['cityList']
for i in range(len(cityList)):
    result.append({
        'name': cityList[i]['name'],
        'code': cityList[i]['code']
    })
    if cityList[i]['subLevelModelList']:
        for j in range(len(cityList[i]['subLevelModelList'])):
            result.append({
                'name': cityList[i]['subLevelModelList'][j]['name'],
                'code': cityList[i]['subLevelModelList'][j]['code']
            })


write_json({'data': result})
# print(result)

import def_fuc as fuc

# 目标网站
url = "https://www.zhipin.com/c101270100-p100999/s_302/?page=1&ka=page-1"
# 模拟浏览器的user-agent
UA = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
headers = {
    'User-Agent': UA
}

bsObj = fuc.getBsObj(url, headers)

fuc.getCompanyInfo(bsObj)

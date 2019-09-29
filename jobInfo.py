import def_fuc as fuc

# 目标网站
URL = "https://www.zhipin.com/c101270100-p100999/s_301/?page="
# 模拟浏览器的user-agent
UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3887.7 Safari/537.36'
cookie = '__c=1569718342; __g=-; __l=l=%2Fwww.zhipin.com%2Fweb%2Fcommon%2Fsecurity-check.html%3Fseed%3Dkp%252BzExuw20Nx%252F%252B1XWHKscH6u%252FvcZEuA%252F2zHgSczW2Fk%253D%26name%3Dd9abeae3%26ts%3D1569718340468%26callbackUrl%3D%252Fc101270100-p100999%252Fs_301%252F%253Fpage%253D1%26srcReferer%3D&r=&friend_source=0&friend_source=0; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1569555372,1569718342,1569721114; lastCity=101010100; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1569724258; t=oPWYNEJi9h5U26Th; wt=oPWYNEJi9h5U26Th; _bl_uid=4Ckkm12O4bkdOCbtFee5mms2s7h6; __zp_stoken__=f25cZJHuDfVNuRcFFY4laQaAadKVMdoYD41POzznGVV38nG%2BdTu8AllTdn8iKDAy%2BxBkKGzAadLBXM1yMECZNxYt4Q%3D%3D; __a=39105322.1569555371.1569555371.1569718342.250.2.247.250'

headers = {
    'User-Agent': UA,
    'cookie': cookie,
    'Connection': 'keep-alive',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Host': 'www.zhipin.com',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Cache-Control': 'max-age=0',
    'Referer': 'https://www.zhipin.com/',
    'Upgrade-Insecure-Requests': '1',
}

# bsObj = fuc.getBsObj(url, headers)
# comInfo = fuc.getCompanyInfo(bsObj)
index = 1
while True:
    url = URL + str(index)

    bsObj = fuc.getBsObj(url, headers)
    comInfo = fuc.getCompanyInfo(bsObj)
    index = index + 1
    print(url)
    # print(bsObj)
    print(comInfo)
    if len(comInfo) == 0:
        break
# print(comInfo)
# fuc.saveDataToMongoDB(comInfo)
# fuc.deleteAllData()

import def_fuc as fuc

# 目标网站
url = "https://www.zhipin.com/c101270100-p100999/s_301/?page=1"
# 模拟浏览器的user-agent
UA = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
cookie = '__c=1569555371; __g=-; __zp_stoken__=e468vkfR72%2Bj%2FyPTfu1I%2BfMaL0R7tjQcFjZnw%2BdIuvvRJwU0Hr%2BJCzdnczyrWiji3o9QVT2s7QmOfI5JmrE61IL2bg%3D%3D; __l=l=%2Fwww.zhipin.com%2Fweb%2Fcommon%2Fsecurity-check.html%3Fseed%3Dkp%252BzExuw20Nx%252F%252B1XWHKscF6ZpcaxLOFomYuHvWvwick%253D%26name%3D4672dc2c%26ts%3D1569555369108%26callbackUrl%3D%252Fc101270100-p100999%252Fs_301%252F%253Fpage%253D1%26srcReferer%3D&r=&friend_source=0&friend_source=0; __a=39105322.1569555371..1569555371.2.1.2.2; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1569555372; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1569555372; __zp_sseed__=kp+zExuw20Nx/+1XWHKscCojNhuXQ6Dau/DjxH2Chss=; __zp_sname__=4672dc2c; __zp_sts__=1569555395667'
headers = {
    'User-Agent': UA,
    'cookie': cookie
}

bsObj = fuc.getBsObj(url, headers)
comInfo = fuc.getCompanyInfo(bsObj)
print(comInfo)
# fuc.saveDataToMongoDB(comInfo)
# fuc.deleteAllData()

from selenium import webdriver
from selenium.webdriver import ChromeOptions
import time

url = 'https://qun.qq.com/member.html'

option = ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])
# 设置中文
option.add_argument('lang=zh_CN.UTF-8')
# 更换头部
option.add_argument('user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"')
browser = webdriver.Chrome(options=option)
browser.get(url)  # 打开浏览器预设网址
browser.maximize_window()
time.sleep(5)
# 手动登陆

# 需要在这里边获取Cookie，bkn，和所有群号码，把所有群号码存起来，然后在爬虫里边一个一个取群号码，Cookie和bkn的值就直接传


cookie = browser.get_cookies()
for lq in cookie:
  if lq["name"] == 'RK':
    RK = lq["value"]
  elif lq["name"] == 'ptcz':
    ptcz = lq["value"]
  elif lq["name"] == 'pgv_pvid':
    pgv_pvid = lq["value"]
  elif lq["name"] == '_qpsvr_localtk':
    _qpsvr_localtk = lq["value"]
  elif lq["name"] == 'uin':
    uin = lq["value"]
  elif lq["name"] == 'skey':
    skey = lq["value"]
  elif lq["name"] == 'p_uin':
    p_uin = lq["value"]
  elif lq["name"] == 'pt4_token':
    pt4_token = lq["value"]
  elif lq["name"] == 'p_skey':
    p_skey = lq["value"]
  elif lq["name"] == 'traceid':
    traceid = lq["value"]
# 拼接Cookies
cookies = 'RK='+RK+'; '+'ptcz='+ptcz+'; '+'_qpsvr_localtk='+_qpsvr_localtk+'; '+'uin='+uin+'; '\
          +'skey='+skey+'; '+'p_uin='+p_uin+'; '+'pt4_token='+pt4_token+'; '+'p_skey='+p_skey+'; '\
          +'traceid='+traceid+'; '


print(cookies)





# 执行js语句，然后获取bkn的返回值
# 获取bkn参数

bkn = browser.execute_script('return $.getCSRFToken()')


file1 = open('ck.text', 'w')
file2 = open('bkn.text', 'w')
file1.write(cookies)
file2.write(str(bkn))
file1.close()
file2.close()

browser.close()
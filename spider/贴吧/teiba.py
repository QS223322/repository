from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import time
import re

# 贴吧主页
ck = [{'name': 'BAIDUID', 'value': 'CECE8A1DFA1CA70868C4C54B333F6EA8:FG=1', 'path': '/', 'domain': '.baidu.com', 'secure': False, 'httpOnly': False, 'expiry': 1714898978, 'sameSite': 'None'}, {'name': 'BAIDU_WISE_UID', 'value': 'wapp_1683362980678_406', 'path': '/', 'domain': '.baidu.com', 'secure': False, 'httpOnly': False, 'expiry': 2629442980, 'sameSite': 'None'}, {'name': 'USER_JUMP', 'value': '-1', 'path': '/', 'domain': 'tieba.baidu.com', 'secure': False, 'httpOnly': False, 'sameSite': 'None'}, {'name': 'st_key_id', 'value': '17', 'path': '/', 'domain': 'tieba.baidu.com', 'secure': False, 'httpOnly': False, 'sameSite': 'None'}, {'name': 'FPTOKEN', 'value': 'Wb5K5b9+CpKPMBJK+n0JeCP7CR+rehEL0HoGx3rkWyo0dVrXv4Z0IW4QrzdUMVVtJfKL92lKo3KdpCGTlKZ4D+mi38UrmitS2mZLf2YVEG7i6R/pcNRjyJ8oJQIDtbQOZFIFZJl1l3vOhM8C8u/dCw3XAdRxoXdA9jT2comzEODmY1ehHTyAjyOCZ+2/qaUniitmYpx2lLuVe/JEmDVhcwciJvzKrhbmzutA2WxRM6z/mzWZfETA2BBaDOz9hhiraOSouZKL9afzDcGB5TE/n6KQM52erdknzfxM3YlzkxgusxjdECbKThQIWufJbayyCS4xVhLUXoXUu8+U6n2KNc67MaAcRZDI24kGhkpX1PzSlXIIO1OEDdphEcBTLcabp7F7R1WA7gQBNXMtRWtc/Q==|GmPWuM0iTFEZ4J8l1itDWhZit3dUei98x2B7+iiqfkw=|10|820c67b3279c0a6190fdb8e6acbbcf7b', 'path': '/', 'domain': '.baidu.com', 'secure': False, 'httpOnly': False, 'expiry': 2547362982, 'sameSite': 'None'}, {'name': 'arialoadData', 'value': 'false', 'path': '/', 'domain': '.baidu.com', 'secure': False, 'httpOnly': False, 'expiry': 1683449382, 'sameSite': 'None'}, {'name': 'BDUSS', 'value': 'VlZ3pzVklyUml-MjlTZH55Qkg2a0ZJWldXcHFHYTE4Ni15UGFRTmFvYThvWDFrRVFBQUFBJCQAAAAAAAAAAAEAAABFnuQfOTk3NTEzNDM1AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALwUVmS8FFZkNG', 'path': '/', 'domain': '.baidu.com', 'secure': False, 'httpOnly': True, 'expiry': 1942563004, 'sameSite': 'None'}, {'name': 'STOKEN', 'value': 'f10f1d8e69c07123dda1e0eff0996d29ceb95659ec2eb305074157e6b031d41f', 'path': '/', 'domain': '.tieba.baidu.com', 'secure': False, 'httpOnly': True, 'expiry': 1685955005, 'sameSite': 
'None'}, {'name': '__bid_n', 'value': '187f040a3d8d5275ab4207', 'path': '/', 'domain': '.baidu.com', 'secure': False, 'httpOnly': False, 'expiry': 1998723006, 'sameSite': 'None'}, {'name': 'ab_sr', 'value': '1.0.1_NjExYzRkY2M5NDQ4NjBlNzZjMzM2NTVjODY0MWU1ZmU4YjQzNzQwZTkxYzM5NzE4MzdhZDlhMWY3MGYxNjU2MzM0MmQ0ZTY4NmY3ZWZiODczNzI1OWFjNmJmYTA1MmIxZDlkYjU3MjdlNzMwZDZjMDZiMTQ0NTE4ODMyYTRjYzgzZTk3NDdkMTgzYjQ2NWI3YTc1ZDNhMmY1MTExYTZjODg5NzJkZTA4NWYxNDExMWZlNDYxNGM0ODM2N2ExM2M3', 'path': '/', 'domain': '.baidu.com', 'secure': True, 'httpOnly': True, 'expiry': 1683370206, 'sameSite': 'None'}, {'name': 'XFI', 'value': 'ffe648b0-ebea-11ed-a4d5-ebb1ec1d34f3', 'path': 
'/', 'domain': 'tieba.baidu.com', 'secure': False, 'httpOnly': False, 'sameSite': 'None'}, {'name': 'Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948', 'value': '1683362981', 'path': '/', 'domain': '.tieba.baidu.com', 'secure': False, 'httpOnly': False, 'expiry': 1714899006, 'sameSite': 'None'}, {'name': 'Hm_lpvt_98b9d8c2fd6608d564bf2ac2ae642948', 'value': '1683363007', 'path': '/', 'domain': '.tieba.baidu.com', 'secure': False, 'httpOnly': False, 'sameSite': 'None'}, {'name': 'st_data', 'value': '709639709391ece9f3d20dac22db4e51ab40d9f64d34ddab9f4141e4931455611d46729ddfbc7331b3a9526f3e74db0af193ad1e69590a36cf308fd0250ad138f5fde00aa363780a5967f446f2926a569028256f977dab91c28e9325eae462fa', 'path': '/', 'domain': 'tieba.baidu.com', 'secure': False, 'httpOnly': False, 'sameSite': 'None'}, {'name': 'st_sign', 'value': 'f2c67b14', 'path': '/', 'domain': 'tieba.baidu.com', 'secure': False, 'httpOnly': False, 'sameSite': 'None'}, {'name': 'XFCS', 'value': 'EEABA2AC1B2C03BC48D279D0A2106E00C18E9D1B21CBD7F78D9973AED747422C', 'path': '/', 'domain': 'tieba.baidu.com', 'secure': False, 'httpOnly': False, 'sameSite': 'None'}, {'name': 'XFT', 'value': 'bT7OCyyg60BXA/68tP3gInaWYnnWwZCWGSSiUoQW90Q=', 'path': '/', 'domain': 'tieba.baidu.com', 'secure': False, 'httpOnly': False, 'sameSite': 'None'}, {'name': 'RT', 'value': '"z=1&dm=baidu.com&si=1bc42624-1ad2-41cc-aa95-0885eef89393&ss=lhbquqs4&sl=6&tt=6d2&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=nxl"', 'path': '/', 'domain': '.baidu.com', 'secure': False, 'httpOnly': False, 'expiry': 1683967809, 'sameSite': 'Lax'}]

binary = FirefoxBinary(r'C:\\Program Files\\Mozilla Firefox\\firefox.exe')
diver = webdriver.Firefox(firefox_binary=binary)
diver.get('https://tieba.baidu.com/index.html')
for i in ck:
    diver.add_cookie(i)

def save(ls, f, idx):
    for i in ls:
        f.write('{}\n'.format(i[idx]))

for i in range(30):
    diver.get("https://tieba.baidu.com/f?kw=%E6%94%80%E6%9E%9D%E8%8A%B1&ie=utf-8&pn={}".format(i*50))
    time.sleep(1.5)
    content = diver.page_source
    tx = re.findall('<a rel="noopener" href="/p/(.*?)" title="(.*?)" target="_blank" class="j_th_tit ">',content, re.S)
    with open("test1.txt",'a', encoding='utf-8') as f:
        save(tx, f, 1)
        f.close()
    with open("test2.txt",'a', encoding='utf-8') as f:
        save(tx, f, 0)
        f.close()
    print(i*50)
diver.close()



# 单贴
binary = FirefoxBinary(r'C:\\Program Files\\Mozilla Firefox\\firefox.exe')
diver = webdriver.Firefox(firefox_binary=binary)
script = 'Object.defineProperty(navigator,"webdriver",{get:() => undefined,});'
diver.execute_script(script)

def spider(url):
        try:
                diver.get(f'https://tieba.baidu.com/p/{url}')
                res = diver.page_source
                ls = re.findall('style="display:;">(.*?)</div>',res, re.S)
                print(ls[1])

        except:
                time.sleep(30)        
                diver.get(f'https://tieba.baidu.com/p/{url}')
                res = diver.page_source
                ls = re.findall('style="display:;">(.*?)</div>',res, re.S)


        return ls

def save(ls, f, t):
        f.write('{}\n'.format(t))
        for i in ls:
                i = i.replace(" ", "")
                str = re.sub('<.*?>', '', i)
                f.write('{}\n'.format(str))
f1 = open("test1.txt", "r", encoding='utf-8')
f2 = open("test2.txt", "r", encoding='utf-8')
f = open('text.txt', 'a', encoding='utf-8')
num = 1495
for i in range(num):
        t1 = f1.readline()
        t2 = f2.readline()
        if(len(t1)<4):
                continue
        else:
                ls = spider(t2)
                print(ls[1])
                save(ls[1::2], f, t1)
                print(i)
f1.close()
f2.close()
f.close()
diver.close()
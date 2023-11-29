# import requests
# import json
#
#
# while True:
#     word = input('请输入你要翻译的内容：')
#     url = 'http://fanyi.youdao.com/translate'
#     headera = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'}
#     data = {
#     'i': word,
#     'doctype': 'json',
#     }
#     response = requests.post(url,headers=headera,data=data)
#     dict_str = json.loads(response.content.decode())
#     tran = dict_str['translateResult'][0][0]['tgt']
#     print(tran)
#     if word == '1':
#         break

import hashlib
import time
import random
import requests

headers = {
    'Cookie': 'OUTFOX_SEARCH_USER_ID=-2006006658@10.108.160.17; OUTFOX_SEARCH_USER_ID_NCOO=637053778.397833; UM_distinctid=174569dbd3e165-064df79033d73e-f7b1332-144000-174569dbd3f4e1; P_INFO=13738726398|1599483534|1|youdaodict|00&99|null&null&null#gud&440400#10#0|&0|null|13738726398; DICT_PERS=v2|urs-phone-web||DICT||web||604800000||1599483535136||223.73.72.95||urs-phoneyd.4f432dfaa2aa42039@163.com||JFRfzA6LqS0JzhMqu6MYW0k5OfQLOLqu0k5hHYGO4gBRlAhLwLhLPBRPy6MzWO4P4RQZhMgShHgz0qBhfeBRHOM0; JSESSIONID=aaakOLhlG98n3_GHGYTrx; DICT_SESS=v2|l_MaOezpZ0k5kfJuO4PLRk5Rfp4k4eLRTB0LJF0MJLRPuRLPBn4Ul0pL0MTFOfzm0UG0MkfkMPy0pFhHJBRfq40lfPLOWOfUG0; DICT_LOGIN=3||1599569791389; ___rl__test__cookies=1599569917583',
    'Origin': 'http://fanyi.youdao.com',
    'Referer': 'http://fanyi.youdao.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
}
ua = "5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"

def func(word):
    r = str(int(time.time()*1000))
    t = hashlib.md5(ua.encode('utf-8')).hexdigest()
    i = str(int(r)+random.randint(0, 9))
    return {
        'ts': r,
        'bv': t,
        'salt': i,
        'sign': hashlib.md5(("fanyideskweb" + word + i + "Tbh5E8=q6U3EXe+&L[4c@").encode('utf-8')).hexdigest()
    }

def data(word):
    r = func(word)
    return{
    'i': word,
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'salt': r['salt'],
    'sign':r['sign'],
    'lts': r['ts'],
    'bv': r['bv'],
   'doctype': 'json',
    'version': '2.1',
   'keyfrom': 'fanyi.web',
    'action': 'FY_BY_CLICKBUTTION'
    }

def run():
    url ="http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
    Word = input()
    if (Word=="q"):
        exit()
    response = requests.post(url, headers=headers, data=data(Word))
    # print(response.text)
    try:
        content = response.json()['translateResult'][0][0]
        sentences = response.json()['translateResult'][0]
        src = content['src']
        if response.json()['smartResult']:
            means = response.json()['smartResult']['entries']
            print(f"\n\n查询:{src}\n翻译内容为:")
            for i in means[1:]:
                print("\t", i, end="")
            print("\n\n")
    except:
        try:
            print("\n\n")
            for sentence in sentences:
                print(f"查询:{sentence['src']}\n翻译内容为:{sentence['tgt']}")
            print("\n\n")
        except:
            print("\n\n不存在该单词\n\n")
if __name__ =="__main__":
    print("*" * 50)
    print("如果 退出请输入q")
    print("*" * 50)
    while(True):
        print("输入需要翻译的文字:", end="")
        run()

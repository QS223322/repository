import requests
import execjs

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64;` rv:47.0) Gecko/20100101 Firefox/47.0",
    "referer": "https://www.newrank.cn/public/news.html?",
}

with open(r"C:\Users\q's\WebstormProjects\untitled\test.js", encoding='utf-8') as f:
    # 上面这个newrank.js文件就是我们新建的js文件，里面放入了从网站JS源码抠出的两个函数。
    js = f.read()
    ctx = execjs.compile(js)

for page in range(1, 2):
    nonce = ctx.call('j')  # 调用JS代码中的函数生成第一个加密参数nonce
    xyz = f'/xdnphb/index/getMedia?AppKey=joker&keyword=&pageNumber={page}&pageSize=10&nonce=' + nonce
    xyz = ctx.call('b', xyz)  # 调用JS代码中的函数生成第二个加密参数xyz
    # xyz参数也可以直接用python的MD5加密实现
    # xyz=hashlib.md5(xyz.encode(encoding='utf-8')).hexdigest()
    data = {
        'keyword': '',
        'pageNumber': str(page),
        'pageSize': '10',
        'nonce': nonce,
        'xyz': xyz
    }
    # print(nonce, xyz)
    response = requests.post('https://www.newrank.cn/xdnphb/index/getMedia', headers=headers, data=data)
    print(response.status_code)
    # print(response.text)
    response_data = response.json()['value']
    # pprint.pprint(response_data)
    for item in response_data:
        print('资讯标题:', item['title'], '发布时间：', item['public_time'])

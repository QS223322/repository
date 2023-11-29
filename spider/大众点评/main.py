# coding:utf-8
import re
import requests
from fontTools.ttLib import TTFont  # coding:utf-8
import xlwt
import xlrd
from xlutils.copy import copy

class Public_Spider():
    def __init__(self):
        self.ur = 'http://www.dianping.com/shop/'
        self.head = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            # cookie需要更换为你登录的Cookie
            'Cookie': 'navCtgScroll=0; fspop=test; _lx_utm=utm_source%3Dbing%26utm_medium%3Dorganic; _lxsdk_cuid=17ccbf4bbb7c8-0acd7ce5f8b454-561a145a-144000-17ccbf4bbb7c8; _lxsdk=17ccbf4bbb7c8-0acd7ce5f8b454-561a145a-144000-17ccbf4bbb7c8; _hc.v=66a99ade-ab36-acf8-d4f0-9c9153bfa723.1635509386; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1635509387; _dp.ac.v=f490ec1e-23b8-480b-af5f-0a0f95b01cb7; dplet=b58073f0475d5d8ad5c734ff8f39de80; dper=238bd2487642462233a2a31da40d74ff68e08f28f803065c4591a3100e550f02812b083e7dc0f89a856703b5e26db34f27034f0f7a439788a8dcca41f8c29f11e03dce85d4928870d4d53d756889773b3a4facf2e7c1f7780129d49f4fabb58f; ll=7fd06e815b796be3df069dec7836c3df; ua=dpuser_0312013790; ctu=3d65cb1519d374b58228467c800820b7488ba9d5669c617e358fb088f0c256c2; uamo=13628160208; cy=9; cye=chongqing; s_ViewType=10; _lxsdk_s=17ccbf4bbb7-a3d-0fc-564%7C%7C126; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1635509473',
            'Host': 'www.dianping.com',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36',
            }

    def Get_html(self, i):
        if i != 1:
            response = requests.get(url="http://www.dianping.com/chongqing/ch10/g110o2p{}".format(i), headers=self.head).content.decode('utf-8')
        else:
            response = requests.get(url="http://www.dianping.com/chongqing/ch10/g110o2", headers=self.head).content.decode('utf-8')
        # print(response)
        self.html = re.sub('\s', '', response)

    def Get_TTF(self):
        TTF = re.findall('<linkrel="stylesheet"type="text\/css"href="(.*?)">', self.html, re.S)[1]  # 缩小范围，店铺信息
        header = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36", }
        res = requests.get('http:' + TTF, headers=header).text
        TTF_dict = {}
        fontlist = re.findall('@font-face{(.*?)}', res, re.S)
        for font in fontlist:
            TTF_name = re.findall('font-family: "PingFangSC-Regular-(.*?)"', font, re.S)[0]
            TTF_link = re.findall(',url\("(.*?)"\);', font, re.S)[0]
            TTF_dict.update({TTF_name: TTF_link})
        shopNum = TTF_dict.get('shopNum')
        tagName = TTF_dict.get('tagName')
        b = requests.get('http:' + shopNum, headers=header).content
        with open('大众点评shopNum.ttf', 'wb') as f:
            f.write(b)
        b = requests.get('http:' + tagName, headers=header).content
        with open('大众点评tagName.ttf', 'wb') as f:
            f.write(b)
        font1 = TTFont('大众点评shopNum.ttf')
        uni_list1 = font1.getGlyphOrder()[2:]
        self.utf8List = ['&#x' + uni[3:] for uni in uni_list1]
        font2 = TTFont('大众点评tagName.ttf')
        uni_list2 = font2.getGlyphOrder()[2:]
        self.utf8List2 = ['&#x' + uni[3:] for uni in uni_list2]
        self.wordlist = '1234567890店中美家馆小车大市公酒行国品发电金心业商司超生装园场食有新限天面工服海华水房饰城乐汽香部利子老艺花专东肉菜学福饭人百餐茶务通味所山区门药银农龙停尚安广鑫一容动南具源兴鲜记时机烤文康信果阳理锅宝达地儿衣特产西批坊州牛佳化五米修爱北养卖建材三会鸡室红站德王光名丽油院堂烧江社合星货型村自科快便日民营和活童明器烟育宾精屋经居庄石顺林尔县手厅销用好客火雅盛体旅之鞋辣作粉包楼校鱼平彩上吧保永万物教吃设医正造丰健点汤网庆技斯洗料配汇木缘加麻联卫川泰色世方寓风幼羊烫来高厂兰阿贝皮全女拉成云维贸道术运都口博河瑞宏京际路祥青镇厨培力惠连马鸿钢训影甲助窗布富牌头四多妆吉苑沙恒隆春干饼氏里二管诚制售嘉长轩杂副清计黄讯太鸭号街交与叉附近层旁对巷栋环省桥湖段乡厦府铺内侧元购前幢滨处向座下澩凤港开关景泉塘放昌线湾政步宁解白田町溪十八古双胜本单同九迎第台玉锦底后七斜期武岭松角纪朝峰六振珠局岗洲横边济井办汉代临弄团外塔杨铁浦字年岛陵原梅进荣友虹央桂沿事津凯莲丁秀柳集紫旗张谷的是不了很还个也这我就在以可到错没去过感次要比觉看得说常真们但最喜哈么别位能较境非为欢然他挺着价那意种想出员两推做排实分间甜度起满给热完格荐喝等其再几只现朋候样直而买于般豆量选奶打每评少算又因情找些份置适什蛋师气你姐棒试总定啊足级整带虾如态且尝主话强当更板知己无酸让入啦式笑赞片酱差像提队走嫩才刚午接重串回晚微周值费性桌拍跟块调糕'

    def Get_url(self, name):
        shop_info = re.findall('<liclass="">(.*?)<\/li>', self.html, re.S)
        for i in range(len(shop_info)):
            # try:
                star = re.findall('class="starstar_(.*?)star_sml"', shop_info[i], re.S)[0]
                star = (int(star)/10)
                shop_name = re.findall('data-name="(.*?)"', shop_info[i], re.S)
                # shop_url = re.findall('data-shopid="(.*?)"', shop_info[i], re.S)[0]
                shop_goods = re.findall('target="_blank">(.*?)<\/a>', shop_info[i], re.S)
                coment = re.findall('<b>(.*?)<\/b>条评价', shop_info[i], re.S)[0]
                # per_capita = re.findall('人均<b>(.*?)<\/b', shop_info[i], re.S)
                per_capita = re.findall('"shopNum">(.*?)</svgmtsi>', shop_info[i], re.S)
                # print(per_capita)
                tag = '|'.join(re.findall('<spanclass="tag">(.*?)<\/span>', shop_info[i], re.S))
                # quests_url = 'http://www.dianping.com/ajax/json/shopDynamic/allReview?shopId={}&cityId=9&shopType=10&tcv=o2802z56k0&_token=eJx1kFtvgkAQhf%2FLvnYDu8t1SXwwihfEWkFsqPFBkQLlquAFm%2F73Do196EOTTeY7Z05mJvuJTtMDMighRKYYXcITMhAViKAijJoaOqqkKISrGtEUBaPgj0cljWG0P62HyNhwnWFNVred4YDeUEVSsa7KW%2FxACk0mw%2BsyU4iguGkqQxSv16twSHZFlRSREJS5WMdlJWa6ZfvVwCPmxOJTTYOL%2FssHcVlER1BAlIgRpaRkCNbkq24N1wmWlG4AZwwznXdEOWb8x6MSkNwRges4BdK5AjmtG5F2I6DuHrX51XP4KojWSVQAhdZt5dZyfXx35vV%2B7bUtn7kua%2B2A2q4n2Xezefbcy6Id6H337PjhS2aOPpLJ%2BBSr4ShT8%2Bo8vHnz44BazXApeUna3IPbwp5diBvQhXOw%2FDTjRT6mqT8evb7lubef9c3%2B%2BSmIpWWvh76%2BAWhvgY8%3D&uuid=66a99ade-ab36-acf8-d4f0-9c9153bfa723.1635509386&platform=1&partner=150&optimusCode=10&originUrl=http%3A%2F%2Fwww.dianping.com%2Fshop%2Fl8JLYpCU0EHJ9I77'.format(shop_url)
                # star_url = 'http://www.dianping.com/ajax/json/shopDynamic/reviewAndStar?shopId={}&cityId=9&mainCategoryId=32733&_token=eJx1kElvwjAQhf%2BLz1ZiO7ZjR%2BoBKBKhLFVYSos4kJAmFMiC07JU%2Fe8dV%2FTQQyVL8703TzMjf6JjuEEBJYRwitFHekQBog5xJMKoMdCRnhBES5%2F4QmCU%2FPGo5%2FkYxcf5PQqWWjHsc7myRgR6SYUnsZJ8hW9Iock4PJsJIYLypqkC1z2dTs5muy6qbZE5SXlwTV5W7l71B89VZ0a6vb4OfR8u%2Bi%2Bf5GWR1aCAKHEzSknJEKw5TO0arQj2hB2gGcNMaUtUY6Z%2FPOoBcUsErtMUSGkBOd%2BO2NkRUNe32vzqIXwVRM02K4DS%2Fnk6MdzUr9HQxPPZhXjDa280HnT3o%2BtFdTpRFh8iE9fneSHaSWs83T0t3mTUTmTernm6qNapeH95aLUei%2B4ivENf34epcVU%3D&uuid=66a99ade-ab36-acf8-d4f0-9c9153bfa723.1635509386&platform=1&partner=150&optimusCode=10&originUrl=http%3A%2F%2Fwww.dianping.com%2Fshop%2Fl8JLYpCU0EHJ9I77'.format(shop_url)
                # evaluate = self.Get(quests_url)
                # evaluate_list = []
                # for k in evaluate.get('summarys'):
                #     evaluate_list.append(k.get('summaryString'))
                # star = self.Get(star_url)
                # star = star.get('fiveScore')
                for i in range(10):
                    coment = coment.replace(self.utf8List[i], self.wordlist[i])  # 字体映射
                    per_capita = ''.join(per_capita).replace(self.utf8List[i], self.wordlist[i])  # 字体映射
                    # print(per_capita)
                shop_comment = (''.join(re.findall('\d', coment, re.S)))  # 评价数目
                per_capita = (''.join(re.findall('\d', per_capita, re.S)))  # 人均消费
                for i in range(len(self.utf8List2)):
                    if self.utf8List2[i] in tag:
                        tag = tag.replace(self.utf8List2[i], self.wordlist[i])
                tag = tag.split('|')
                Tag = []  # 标签列表
                for tag in tag:
                    Tag.append(''.join(re.findall('[\u4e00-\u9fa5]', tag, re.S)))  # 确实只匹配中文
                # print(tag)
                Tag = ' | '.join(Tag)
                workbook = xlrd.open_workbook(name)
                sheets = workbook.sheet_names()  # 获取工作簿中的所有表格
                worksheet = workbook.sheet_by_name(sheets[0])  # 获取工作簿中所有表格中的的第一个表格
                rows_old = worksheet.nrows  # 获取表格中已存在的数据的行数
                new_workbook = copy(workbook)  # 将xlrd对象拷贝转化为xlwt对象
                new_worksheet = new_workbook.get_sheet(0)
                new_worksheet.write(rows_old, 0, str(shop_name[0]))
                new_worksheet.write(rows_old, 1, str(shop_comment))
                new_worksheet.write(rows_old, 2, str(per_capita))
                new_worksheet.write(rows_old, 3, str(Tag))
                new_worksheet.write(rows_old, 4, str(','.join(shop_goods)))
                # new_worksheet.write(rows_old, 5, str(' '.join(evaluate_list)))
                new_worksheet.write(rows_old, 5, str(star))
                new_workbook.save(name)
                print('ok')
            # except:
            #     pass

    def run(self):
        name = '大众点评.xls'
        book = xlwt.Workbook(encoding='utf-8', style_compression=0)
        sheet = book.add_sheet('大众点评')  # 在工作簿中新建一个表格
        list = ['店铺名', '评价数', '人均消费', '类型和地址', '特色菜品', '星级评分']
        for i in range(6):
            sheet.write(0, i, list[i])
        book.save(name)
        for i in range(1, 37):
            self.Get_html(i)
            self.Get_TTF()
            self.Get_url(name)
            print(i)
            # time.sleep(1)

if __name__ == '__main__':
    example = Public_Spider()
    example.run()
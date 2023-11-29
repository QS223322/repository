import random
import requests
import json
import csv

def get_qun(headers, bkn):

    bkn = {
        'bkn': bkn
    }
    qunid = []
    qunname = []
    ponse = requests.post(url='https://qun.qq.com/cgi-bin/qun_mgr/get_group_list', headers=headers, data=bkn)
    a = json.loads(ponse.text)
    for quid in a["join"]:
        qunid.append(quid['gc'])
        # print(quid['gc'])
        qunname.append(quid['gn'])
        # print(quid['gn'])


    return qunid, qunname

def get_other(headers, bkn, num):

    json_data={
        'gc': num,
        'st': 0,
        'end': 20,
        'sort': '0',
        'bkn': bkn
    }
    ponse = requests.post(url='https://qun.qq.com/cgi-bin/qun_mgr/search_group_members',
                          headers=headers, data=json_data)
    ponse.encoding=ponse.apparent_encoding
    a = json.loads(ponse.text)
    person = a["count"]
    leader = a['mems'][0]['nick']
    return person, leader


if __name__ == '__main__':
    c = open('ck.text')
    ck = c.read()
    bk = open('bkn.text')
    bkn = bk.read()

    user_agent = [
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
        "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0",
        "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)",
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
        "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
        "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
        "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"]

    headers = {
        'User-Agent': user_agent[random.randint(0, len(user_agent) - 1)],
        'Cookie': ck
    }

    json_data = {
        'bkn': bkn
    }

    qunid, qunname = get_qun(headers, json_data)
    person, leader = [], []
    for i in qunid:
        p, l = get_other(headers, bkn, i)
        person.append(p)
        leader.append(l)
    c.close()
    bk.close()
    print(qunid)

    file = open('result_.csv', 'w', encoding='utf-8')
    csv_writer = csv.writer(file)
    csv_writer.writerow(["群名", "群号", "群主", "人数"])
    for i in range(0, 30):
        print(i)
        csv_writer.writerow([qunname[i], qunid[i], leader[i], person[i]])
    print('success')
    file.close()
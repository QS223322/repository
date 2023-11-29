import requests
import blackboxprotobuf

url = 'https://s.wanfangdata.com.cn/SearchService.SearchService/search'

deserialize_data = {
  "1": {
    "1": "periodical",
    "2": "百度",
    "5": 1,
    "6": 20,
    "8": "\u0000"
  },
  "2": 1
}

message_type = {'1': {'type': 'message', 'message_typedef': {'1': {'type': 'bytes', 'name': ''}, '2': {'type': 'bytes', 'name': ''}, '5': {'type': 'int', 'name': ''}, '6': {'type': 'int', 'name': ''}, '8': {'type': 'bytes', 'name': ''}}, 'name': ''}, '2': {'type': 'int', 'name': ''}}

headers = {
  'accept': '*/*',
  'accept-encoding': 'gzip, deflate, br',
  'accept-language': 'zh-CN,zh;q=0.9',
  'content-type': 'application/grpc-web+proto',
  'referer': 'https://s.wanfangdata.com.cn/periodical?q=%E7%99%BE%E5%BA%A6',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36',
  'Connection': 'close'
}

form_data = bytes(blackboxprotobuf.encode_message(deserialize_data, message_type))
form_data = bytes([0, 0, 0, 0, len(form_data)])+form_data
print(form_data)
res = requests.post(url, headers=headers, data=form_data, timeout=20, verify=False)
data, type = blackboxprotobuf.protobuf_to_json(res.content[5:-20])
print(data)

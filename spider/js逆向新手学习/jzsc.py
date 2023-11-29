import json
from binascii import a2b_hex
import requests
from Crypto.Cipher import AES

data_url = 'http://jzsc.mohurd.gov.cn/api/webApi/dataservice/query/comp/list?pg=%s&pgsz=15&total=450'


def get_encrypted_data(page):
    """
      , f = d.a.enc.Utf8.parse("jo8j9wGw%6HbxfFn")
          , m = d.a.enc.Utf8.parse("0123456789ABCDEF");
        function h(t) {
            var e = d.a.enc.Hex.parse(t)
              , n = d.a.enc.Base64.stringify(e)
              , a = d.a.AES.decrypt(n, f, {
                iv: m,
                mode: d.a.mode.CBC,
                padding: d.a.pad.Pkcs7
            })
    """
    headers = {
        'Host': 'jzsc.mohurd.gov.cn',
        'Referer': 'http://jzsc.mohurd.gov.cn/data/company',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    encrypted_data = requests.get(url=data_url % page, headers=headers).text
    print(encrypted_data)
    return encrypted_data


def get_decrypted_data(encrypted_data):
    aes = AES.new('jo8j9wGw%6HbxfFn'.encode('utf-8'), AES.MODE_CBC, '0123456789ABCDEF'.encode('utf-8'))
    decrypted_data = aes.decrypt(a2b_hex(encrypted_data))
    return json.loads(decrypted_data)


def main():
    for page in range(1):
        encrypted_data = get_encrypted_data(page)
        decrypted_data = get_decrypted_data(encrypted_data)
        print(decrypted_data['data']['list'])


if __name__ == '__main__':
    main()

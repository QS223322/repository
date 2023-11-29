import execjs


ctx = execjs.compile(r"""
function getDecryptedData(t) {
  var CryptoJS = require('crypto-js'),
    m = CryptoJS.enc.Utf8.parse('0123456789ABCDEF'),
    f = CryptoJS.enc.Utf8.parse('jo8j9wGw%6HbxfFn'),
    e = CryptoJS.enc.Hex.parse(t),
    n = CryptoJS.enc.Base64.stringify(e),
    a = CryptoJS.AES.decrypt(n, f, {
      iv: m,
      mode: CryptoJS.mode.CBC,
      padding: CryptoJS.pad.Pkcs7
    }),
    r = a.toString(CryptoJS.enc.Utf8);
  return r.toString();
}

// 测试样例
var t = '95780ba094xxxxxxxxxx';
console.log(getDecryptedData(t));

""")
print(ctx.call("getDecryptedData", '95780ba094xxxxxxxxxx'))

'''
var  CryptoJS = require('C:\\Users\\q\'s\\node_modules\\crypto-js');
function c(t, e) {
  var a = CryptoJS.enc.Utf8.parse(e);
  try {
    var s = CryptoJS.DES.encrypt(String(t), a, {
      mode: CryptoJS.mode.ECB,
      padding: CryptoJS.pad.Pkcs7
    })
  } catch (t) {
    console.log(t)
  }
  return s.toString();
}
console.log(c('xx223322', 'e9284d45-cf2a-4e46-9367-f122413ca6b0'));
'''

url = 'https://cj.eloancn.com/user/login?service=https%3A%2F%2Fcj.eloancn.com%2Fpcgway%2Fapp001%2Fv1%2F02%3Fret%3DaHR0cHM6Ly9jai5lbG9hbmNuLmNvbQ%3D%3D&v=1621670639475'
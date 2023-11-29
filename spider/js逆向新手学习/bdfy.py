import execjs
import requests

# u = null !== i ? i : (i = window[l] || "") || "";
# l = gtk


key = input('输入词：')
ctx = execjs.compile(r"""
var i = '320305.131321201';
function a(r) {
        if (Array.isArray(r)) {
            for (var o = 0, t = Array(r.length); o < r.length; o++)
                t[o] = r[o];
            return t
        }
        return Array.from(r)
    }
    function n(r, o) {
        for (var t = 0; t < o.length - 2; t += 3) {
            var a = o.charAt(t + 2);
            a = a >= "a" ? a.charCodeAt(0) - 87 : Number(a),
            a = "+" === o.charAt(t + 1) ? r >>> a : r << a,
            r = "+" === o.charAt(t) ? r + a & 4294967295 : r ^ a
        }
        return r
    }
    function e(r) {
        var o = r.match(/[\uD800-\uDBFF][\uDC00-\uDFFF]/g);
        if (null === o) {
            var t = r.length;
            t > 30 && (r = "" + r.substr(0, 10) + r.substr(Math.floor(t / 2) - 5, 10) + r.substr(-10, 10))
        } else {
            for (var e = r.split(/[\uD800-\uDBFF][\uDC00-\uDFFF]/), C = 0, h = e.length, f = []; h > C; C++)
                "" !== e[C] && f.push.apply(f, a(e[C].split(""))),
                C !== h - 1 && f.push(o[C]);
            var g = f.length;
            g > 30 && (r = f.slice(0, 10).join("") + f.slice(Math.floor(g / 2) - 5, Math.floor(g / 2) + 5).join("") + f.slice(-10).join(""))
        }
        var u = void 0
          , l = "" + String.fromCharCode(103) + String.fromCharCode(116) + String.fromCharCode(107);
        u = null !== i ? i : (i = window[l] || "") || "";
        for (var d = u.split("."), m = Number(d[0]) || 0, s = Number(d[1]) || 0, S = [], c = 0, v = 0; v < r.length; v++) {
            var A = r.charCodeAt(v);
            128 > A ? S[c++] = A : (2048 > A ? S[c++] = A >> 6 | 192 : (55296 === (64512 & A) && v + 1 < r.length && 56320 === (64512 & r.charCodeAt(v + 1)) ? (A = 65536 + ((1023 & A) << 10) + (1023 & r.charCodeAt(++v)),
            S[c++] = A >> 18 | 240,
            S[c++] = A >> 12 & 63 | 128) : S[c++] = A >> 12 | 224,
            S[c++] = A >> 6 & 63 | 128),
            S[c++] = 63 & A | 128)
        }
        for (var p = m, F = "" + String.fromCharCode(43) + String.fromCharCode(45) + String.fromCharCode(97) + ("" + String.fromCharCode(94) + String.fromCharCode(43) + String.fromCharCode(54)), D = "" + String.fromCharCode(43) + String.fromCharCode(45) + String.fromCharCode(51) + ("" + String.fromCharCode(94) + String.fromCharCode(43) + String.fromCharCode(98)) + ("" + String.fromCharCode(43) + String.fromCharCode(45) + String.fromCharCode(102)), b = 0; b < S.length; b++)
            p += S[b],
            p = n(p, F);
        return p = n(p, D),
        p ^= s,
        0 > p && (p = (2147483647 & p) + 2147483648),
        p %= 1e6,
        p.toString() + "." + (p ^ m)
    }
""")
sign = ctx.call("e", key)
data = {
    'from': 'zh',
    'to': 'en',
    'query': key,
    'transtype': 'realtime',
    'simple_means_flag': 3,
    'sign': sign,
    'token': 'e2d5deacea4adc09bc9543c91ef54edc',
    'domain': 'common'
}

ponse = requests.post('https://fanyi.baidu.com/v2transapi?from=zh&to=en', headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
    'Cookie': 'BIDUPSID=2CC94D8E3E08C2B7C81C229F871E948A; PSTM=1634391470; __yjs_duid=1_221a0ce4e430d3893ea658dd8749ca981634822439711; H_WISE_SIDS=107315_110085_114550_127969_131862_164869_176399_179350_180276_181126_181588_182530_183035_183330_184010_184441_186316_186635_186665_186669_186716_186841_186897_187346_187449_187485_187819_188182_188453_188553_188615_188745_188786_188843_188872_189325_189679_189731_189755_190035_190114_190247_190474_190510_190622_190679_190682_190757_190779_190860_191247_191370_191418_191433_191475_191527_191533_191640_191735_191810_192154_192237_192276_192567_192596_192674_192711_192851_192871_192903_193004_193175_193319_193701_193734_193759_8000054_8000108_8000125_8000141_8000146_8000161_8000164_8000168_8000178_8000179_8000186; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BAIDUID=815D93FD49CB72DD70BD5375C5E1F238:FG=1; BDUSS=URUVnlkdy1KT2EyVW9tcUZ2amVDWWJYdm16eFpkVmt2NDlEZ1lnRVRmQmRHdUJoRVFBQUFBJCQAAAAAAAAAAAEAAAD~nKmiMjE1OTM1N3FhegAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAF2NuGFdjbhhY; BDUSS_BFESS=URUVnlkdy1KT2EyVW9tcUZ2amVDWWJYdm16eFpkVmt2NDlEZ1lnRVRmQmRHdUJoRVFBQUFBJCQAAAAAAAAAAAEAAAD~nKmiMjE1OTM1N3FhegAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAF2NuGFdjbhhY; BAIDUID_BFESS=815D93FD49CB72DD70BD5375C5E1F238:FG=1; delPer=0; PSINO=1; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; H_PS_PSSID=; BDRCVFR[w2jhEs_Zudc]=mbxnW11j9Dfmh7GuZR8mvqV; ZD_ENTRY=google; APPGUIDE_10_0_2=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1642845101,1642907978,1642920676; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1642920676; ab_sr=1.0.1_NmQ5Mzk2MTBhOGNjNzg3NTc4ZDgyY2RmN2IzMGE3MDdjZmY4MWJkZTE5MWFkNjMwMzA5OWNkYzQyZDRiZWZlNjk1MTE4NzFhMWViNTY3ZmRmNzVjMTVkYjJkM2ExMzNmZjI0ZWMzNDdjYTViNDk5NzYzYjk2NGY3ZGYyMjY2YzM=',
    'Referer': 'https://fanyi.baidu.com/'
}, data=data)
print(ponse.text)
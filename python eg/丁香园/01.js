


function bytesToHex(e) {
    for (var t = [], n = 0; n < e.length; n++)
        t.push((e[n] >>> 4).toString(16)),
            t.push((15 & e[n]).toString(16));
    return t.join("")
}
function wordsToBytes(e) {
    for (var t = [], n = 0; n < 32 * e.length; n += 8)
        t.push(e[n >>> 5] >>> 24 - n % 32 & 255);
    return t
}
function bytesToWords(e) {
    for (var t = [], n = 0, r = 0; n < e.length; n++,
        r += 8)
        t[r >>> 5] |= e[n] << 24 - r % 32;
    return t
}

i = {
    utf8: {
        stringToBytes: function (e) {
            return i.bin.stringToBytes(unescape(encodeURIComponent(e)))
        },
        bytesToString: function (e) {
            return decodeURIComponent(escape(i.bin.bytesToString(e)))
        }
    },
    bin: {
        stringToBytes: function (e) {
            for (var t = [], n = 0; n < e.length; n++)
                t.push(255 & e.charCodeAt(n));
            return t
        },
        bytesToString: function (e) {
            for (var t = [], n = 0; n < e.length; n++)
                t.push(String.fromCharCode(e[n]));
            return t.join("")
        }
    }
}
a = i
n = a.utf8
s = function (e) {
    e.constructor == String ? e = n.stringToBytes(e) : "undefined" !== typeof r && "function" == typeof r.isBuffer && r.isBuffer(e) ? e = Array.prototype.slice.call(e, 0) : Array.isArray(e) || (e = e.toString());
    var o = bytesToWords(e)
        , i = 8 * e.length
        , a = []
        , s = 1732584193
        , u = -271733879
        , c = -1732584194
        , l = 271733878
        , f = -1009589776;
    o[i >> 5] |= 128 << 24 - i % 32,
        o[15 + (i + 64 >>> 9 << 4)] = i;
    for (var d = 0; d < o.length; d += 16) {
        for (var p = s, h = u, v = c, y = l, g = f, m = 0; m < 80; m++) {
            if (m < 16)
                a[m] = o[d + m];
            else {
                var b = a[m - 3] ^ a[m - 8] ^ a[m - 14] ^ a[m - 16];
                a[m] = b << 1 | b >>> 31
            }
            var _ = (s << 5 | s >>> 27) + f + (a[m] >>> 0) + (m < 20 ? 1518500249 + (u & c | ~u & l) : m < 40 ? 1859775393 + (u ^ c ^ l) : m < 60 ? (u & c | u & l | c & l) - 1894007588 : (u ^ c ^ l) - 899497514);
            f = l,
                l = c,
                c = u << 30 | u >>> 2,
                u = s,
                s = _
        }
        s += p,
            u += h,
            c += v,
            l += y,
            f += g
    }
    return [s, u, c, l, f]
}
u = function (e) {
    var r = wordsToBytes(s(e));
    return  bytesToHex(r)
}


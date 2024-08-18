const Crypto=require("crypto")

function aes_encrypt(e, n, o) {
    var d = "";
    var c = Object(Crypto.createDecipheriv)("aes-128-cbc", n, o);
    return d += c.update(e, "hex", "utf8"),
        d += c.final("utf8")
}

function h(e, path, n, r) {
    var s = n.s
        , d = n.k
        , f = n.l
        , v = n.d
        , h = n.sort
        , k = n.num
        , y = function (content, t, e) {
        for (var a = Array.from(content), n = Array.from(t), r = a.length, o = n.length, d = String.fromCodePoint, i = 0; i < r; i++)
            a[i] = d(a[i].codePointAt(0) ^ n[(i + e) % o].codePointAt(0));
        return a.join("")
    }(function (s, t, path, e) {
        return [s, t, e, path].join("(&&)")
    }(function (t, e) {
        var n = t;
        if (true) {
            var r = [];
            for (var d in n)
                 r.push(n[d]);
            return r.sort(),
                r.join("")
        }
    }(e, r), parseInt((new Date).getTime() / 1e3) - 655876800 - v, path, h), aes_encrypt(s, d, f), k);
    return btoa(y)
}


function date_dict(r,d) {
    let path = '/v1/user/favorite/app'
    let data = {
        s:d.s,
        k:d.k,
        l:d.l,
        d: 0,
        sort: "dd",
        num: 10
    }

    return h(r,path,data,"get")
}
// console.log(date_dict())
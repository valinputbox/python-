require("./04mod.js")
!function() {
    "use strict";
    var e, t, c, n, a, r, s, f, u, i, o, d, b = {}, l = {};
    function h(e) {
        var t = l[e];
        if (void 0 !== t)
            return t.exports;
        var c = l[e] = {
            id: e,
            loaded: !1,
            exports: {}
        }
          , n = !0;
        try {
            console.log("e",e)
            b[e].call(c.exports, c, c.exports, h),
            n = !1
        } finally {
            n && delete l[e]
        }
        return c.loaded = !0,
        c.exports
    }
    window.yuan=h
    h.m = b,
    e = [],
    h.O = function(t, c, n, a) {
        if (c) {
            a = a || 0;
            for (var r = e.length; r > 0 && e[r - 1][2] > a; r--)
                e[r] = e[r - 1];
            e[r] = [c, n, a];
            return
        }
        for (var s = 1 / 0, r = 0; r < e.length; r++) {
            for (var c = e[r][0], n = e[r][1], a = e[r][2], f = !0, u = 0; u < c.length; u++)
                s >= a && Object.keys(h.O).every(function(e) {
                    return h.O[e](c[u])
                }) ? c.splice(u--, 1) : (f = !1,
                a < s && (s = a));
            if (f) {
                e.splice(r--, 1);
                var i = n();
                void 0 !== i && (t = i)
            }
        }
        return t
    }
    ,
    h.n = function(e) {
        var t = e && e.__esModule ? function() {
            return e.default
        }
        : function() {
            return e
        }
        ;
        return h.d(t, {
            a: t
        }),
        t
    }
    ,
    c = Object.getPrototypeOf ? function(e) {
        return Object.getPrototypeOf(e)
    }
    : function(e) {
        return e.__proto__
    }
    ,
    h.t = function(e, n) {
        if (1 & n && (e = this(e)),
        8 & n || "object" == typeof e && e && (4 & n && e.__esModule || 16 & n && "function" == typeof e.then))
            return e;
        var a = Object.create(null);
        h.r(a);
        var r = {};
        t = t || [null, c({}), c([]), c(c)];
        for (var s = 2 & n && e; "object" == typeof s && !~t.indexOf(s); s = c(s))
            Object.getOwnPropertyNames(s).forEach(function(t) {
                r[t] = function() {
                    return e[t]
                }
            });
        return r.default = function() {
            return e
        }
        ,
        h.d(a, r),
        a
    }
    ,
    h.d = function(e, t) {
        for (var c in t)
            h.o(t, c) && !h.o(e, c) && Object.defineProperty(e, c, {
                enumerable: !0,
                get: t[c]
            })
    }
    ,
    h.f = {},
    h.e = function(e) {
        return Promise.all(Object.keys(h.f).reduce(function(t, c) {
            return h.f[c](e, t),
            t
        }, []))
    }
    ,
    h.u = function(e) {
        return 5437 === e ? "static/chunks/5437-55e57eaf00a7e95f.js" : 5772 === e ? "static/chunks/5772-bb96ae8d1dc3d177.js" : 5551 === e ? "static/chunks/5551-5ca8358968c7eb75.js" : 568 === e ? "static/chunks/568-b398c971321eefe2.js" : 1864 === e ? "static/chunks/1864-ee8ffea5219187a7.js" : 3638 === e ? "static/chunks/3638-683543e8134513ac.js" : 4267 === e ? "static/chunks/4267-e59e018ef411e3ba.js" : 4749 === e ? "static/chunks/4749-8d38b1b8572ce1df.js" : 2068 === e ? "static/chunks/2068-08611942b5ad5ef9.js" : 1116 === e ? "static/chunks/1116-0e9b687aecb88e8f.js" : 2307 === e ? "static/chunks/2307-d3fc4170a2ef5f7f.js" : 1216 === e ? "static/chunks/1216-8c32767922748cac.js" : 4328 === e ? "static/chunks/4328-4e6bc9a377dc9e0d.js" : 6268 === e ? "static/chunks/6268-d07dd7d49c64dc07.js" : 5633 === e ? "static/chunks/5633-64c3fc748825d8ca.js" : 7204 === e ? "static/chunks/7204-0cdeb25acca879e6.js" : 2062 === e ? "static/chunks/2062-3efa6c2bb71b6902.js" : 5798 === e ? "static/chunks/5798-3013c52801906031.js" : 5584 === e ? "static/chunks/5584-9c8768e686b26d6e.js" : 1314 === e ? "static/chunks/1314-9148f32034131b1a.js" : 5607 === e ? "static/chunks/5607-8de330633727b28e.js" : 6337 === e ? "static/chunks/6337-127d479a4353072e.js" : 758 === e ? "static/chunks/758-68e45fd3a63b16da.js" : 3219 === e ? "static/chunks/3219-4a878a9e50ebe184.js" : 5867 === e ? "static/chunks/5867-6d83c063c81c4e7a.js" : 793 === e ? "static/chunks/793-6c06494cefafcbb3.js" : 7284 === e ? "static/chunks/7284-dbb2f72e348fff94.js" : 6782 === e ? "static/chunks/6782-c489fbdcddfff4f4.js" : 5455 === e ? "static/chunks/5455-3357b65affd2e7b9.js" : 8213 === e ? "static/chunks/8213-6ad79c9f10cf8cef.js" : "static/chunks/" + e + "." + ({
            1: "1ef1d482d778bcc2",
            1538: "0c1769830c724306",
            1758: "812801825ff420b1",
            1765: "52ca0cd38eba9c73",
            2513: "3c7b5f9afb68f504",
            3052: "0ca3ad2ff8a5981c",
            3092: "d395fc7afd5ebf0e",
            3644: "93eabab19920c8ae",
            3678: "c95921823a9b1309",
            4093: "d97c959fb2c2336c",
            4118: "62730b3b909b1bbf",
            4140: "4b349de1e5ed2506",
            4454: "e6208ec186d79626",
            4857: "7000d395ebdeda27",
            5206: "e3b89938090d1814",
            5545: "2cf0e005a4c70267",
            5725: "dfc320670bc1bb97",
            5734: "43d93fb9cc659c8c",
            6394: "cce6e75f70f35e04",
            7190: "10cf825694751bcf",
            7269: "8717500b80b1a0c9",
            7287: "fc0055284b6966fa",
            7493: "eb8f6a59548a171d",
            7674: "d12aed5ef8015009",
            8292: "c99d037575c81a89",
            8468: "8f6a518de923e7f1",
            8625: "95d73cc567515f49",
            8670: "9e66ec43d1684412",
            8805: "4cf8b6696d8f1224",
            8970: "f336e4cda0b02cfa",
            8977: "0e4bd1a7f2d51016",
            9162: "5890f942c0768c3a",
            9398: "df6d0025531ccc6a",
            9420: "fceda314e307e325"
        })[e] + ".js"
    }
    ,
    h.miniCssF = function(e) {
        return "static/css/" + ({
            1: "32861b2ca577bab6",
            1754: "32861b2ca577bab6",
            2690: "32861b2ca577bab6",
            2699: "32861b2ca577bab6",
            2888: "5fde8b429145d817",
            3497: "32861b2ca577bab6",
            3937: "32861b2ca577bab6",
            4393: "32861b2ca577bab6",
            4814: "32861b2ca577bab6",
            5215: "32861b2ca577bab6",
            5405: "32861b2ca577bab6",
            5844: "8af6571b0a68de1a",
            6368: "dd18791d836e2bc9",
            7113: "32861b2ca577bab6",
            7226: "32861b2ca577bab6",
            7386: "32861b2ca577bab6",
            8585: "cc8d90aa8c156e0f",
            8957: "cc8d90aa8c156e0f"
        })[e] + ".css"
    }
    ,
    h.g = function() {
        if ("object" == typeof globalThis)
            return globalThis;
        try {
            return this || Function("return this")()
        } catch (e) {
            if ("object" == typeof window)
                return window
        }
    }(),
    h.o = function(e, t) {
        return Object.prototype.hasOwnProperty.call(e, t)
    }
    ,
    n = {},
    a = "_N_E:",
    h.l = function(e, t, c, r) {
        if (n[e]) {
            n[e].push(t);
            return
        }
        if (void 0 !== c)
            for (var s, f, u = document.getElementsByTagName("script"), i = 0; i < u.length; i++) {
                var o = u[i];
                if (o.getAttribute("src") == e || o.getAttribute("data-webpack") == a + c) {
                    s = o;
                    break
                }
            }
        s || (f = !0,
        (s = document.createElement("script")).charset = "utf-8",
        s.timeout = 120,
        h.nc && s.setAttribute("nonce", h.nc),
        s.setAttribute("data-webpack", a + c),
        s.src = h.tu(e)),
        n[e] = [t];
        var d = function(t, c) {
            s.onerror = s.onload = null,
            clearTimeout(b);
            var a = n[e];
            if (delete n[e],
            s.parentNode && s.parentNode.removeChild(s),
            a && a.forEach(function(e) {
                return e(c)
            }),
            t)
                return t(c)
        }
          , b = setTimeout(d.bind(null, void 0, {
            type: "timeout",
            target: s
        }), 12e4);
        s.onerror = d.bind(null, s.onerror),
        s.onload = d.bind(null, s.onload),
        f && document.head.appendChild(s)
    }
    ,
    h.r = function(e) {
        "undefined" != typeof Symbol && Symbol.toStringTag && Object.defineProperty(e, Symbol.toStringTag, {
            value: "Module"
        }),
        Object.defineProperty(e, "__esModule", {
            value: !0
        })
    }
    ,
    h.nmd = function(e) {
        return e.paths = [],
        e.children || (e.children = []),
        e
    }
    ,
    h.tt = function() {
        return void 0 === r && (r = {
            createScriptURL: function(e) {
                return e
            }
        },
        "undefined" != typeof trustedTypes && trustedTypes.createPolicy && (r = trustedTypes.createPolicy("nextjs#bundler", r))),
        r
    }
    ,
    h.tu = function(e) {
        return h.tt().createScriptURL(e)
    }
    ,
    h.p = "https://aws-s3.coinglasscdn.com/cg_v3/_next/",
    s = function(e, t, c, n) {
        var a = document.createElement("link");
        a.rel = "stylesheet",
        a.type = "text/css";
        var r = function(r) {
            if (a.onerror = a.onload = null,
            "load" === r.type)
                c();
            else {
                var s = r && ("load" === r.type ? "missing" : r.type)
                  , f = r && r.target && r.target.href || t
                  , u = Error("Loading CSS chunk " + e + " failed.\n(" + f + ")");
                u.code = "CSS_CHUNK_LOAD_FAILED",
                u.type = s,
                u.request = f,
                a.parentNode.removeChild(a),
                n(u)
            }
        };
        return a.onerror = a.onload = r,
        a.href = t,
        document.head.appendChild(a),
        a
    }
    ,
    f = function(e, t) {
        for (var c = document.getElementsByTagName("link"), n = 0; n < c.length; n++) {
            var a = c[n]
              , r = a.getAttribute("data-href") || a.getAttribute("href");
            if ("stylesheet" === a.rel && (r === e || r === t))
                return a
        }
        for (var s = document.getElementsByTagName("style"), n = 0; n < s.length; n++) {
            var a = s[n]
              , r = a.getAttribute("data-href");
            if (r === e || r === t)
                return a
        }
    }
    ,
    u = {
        2272: 0
    },
    h.f.miniCss = function(e, t) {
        u[e] ? t.push(u[e]) : 0 !== u[e] && ({
            1: 1
        })[e] && t.push(u[e] = new Promise(function(t, c) {
            var n = h.miniCssF(e)
              , a = h.p + n;
            if (f(n, a))
                return t();
            s(e, a, t, c)
        }
        ).then(function() {
            u[e] = 0
        }, function(t) {
            throw delete u[e],
            t
        }))
    }
    ,
    i = {
        2272: 0,
        5844: 0
    },
    h.f.j = function(e, t) {
        var c = h.o(i, e) ? i[e] : void 0;
        if (0 !== c) {
            if (c)
                t.push(c[2]);
            else if (/^(2272|5844)$/.test(e))
                i[e] = 0;
            else {
                var n = new Promise(function(t, n) {
                    c = i[e] = [t, n]
                }
                );
                t.push(c[2] = n);
                var a = h.p + h.u(e)
                  , r = Error()
                  , s = function(t) {
                    if (h.o(i, e) && (0 !== (c = i[e]) && (i[e] = void 0),
                    c)) {
                        var n = t && ("load" === t.type ? "missing" : t.type)
                          , a = t && t.target && t.target.src;
                        r.message = "Loading chunk " + e + " failed.\n(" + n + ": " + a + ")",
                        r.name = "ChunkLoadError",
                        r.type = n,
                        r.request = a,
                        c[1](r)
                    }
                };
                h.l(a, s, "chunk-" + e, e)
            }
        }
    }
    ,
    h.O.j = function(e) {
        return 0 === i[e]
    }
    ,
    o = function(e, t) {
        var c, n, a = t[0], r = t[1], s = t[2], f = 0;
        if (a.some(function(e) {
            return 0 !== i[e]
        })) {
            for (c in r)
                h.o(r, c) && (h.m[c] = r[c]);
            if (s)
                var u = s(h)
        }
        for (e && e(t); f < a.length; f++)
            n = a[f],
            h.o(i, n) && i[n] && i[n][0](),
            i[n] = 0;
        return h.O(u)
    }
    ,
    (d = window.webpackChunk_N_E = window.webpackChunk_N_E || []).forEach(o.bind(null, 0)),
    d.push = o.bind(null, d.push.bind(d)),
    h.nc = void 0
}();
// console.log(window.yuan("81354"))
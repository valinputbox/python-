var yuan = {
    username: "yuan",
    age: 22
}
yuan = new Proxy(yuan, {
    get(target, p, receiver) {
        console.log("target: ", target);
        console.log("p: ", p);
        // return window['username'];/// 这里如果这样写. 有递归风险的...
        // return Reflect.get(...arguments);
        return Reflect.get(target, p);
    },
    set(target, p, value, receiver) {
        console.log("设置操作")
        Reflect.set(target, p, value);
    }
});

console.log(yuan.username);
console.log(yuan.age);
yuan.username = "rain"
yuan.age = 18
console.log(yuan.username);
console.log(yuan.age);
require("./02webpack")
function dec(n,s){
    let M=window.yuan(12210)

    return M.gy(n,{
        iv:s
    })
}
function enc(n){
    let M=window.yuan(12210)
    let s= M._A()
    // let n='{"query":"python","cityCode":101020100,"salaryId":"","experienceId":"","pageNum":1,"limit":15}'
    return [M.mA(n,{
        iv:s
    }).replace(/\//g, "_").replace(/\+/g, "-").replace(/=/g, "~"),s]

}
console.log(enc())
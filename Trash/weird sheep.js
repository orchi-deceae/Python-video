let x = 'This is a string'

// for (let i in x) {
//     console.log(i, x[i])
// }

// for (let i of x) {
//     console.log(i)
// }

// // ver 1
// function use(n) {
//     x_ += n[0]
//     x =  n[2] + n[1] + n[0]
//     x === 'str' ? x_ += '<span>':x=x;
//     return x_
// }

// ver 2
function use(n) {
    x =  n[2] + n[1] + n[0]
    if (x === 'str') {x_ += '<span>'}
    x_ += n[2]
    return x_
}
let a = ''
let x_ = ''
let n = ['', '', '']
for (let i of x) {
    n[2] = n[1]
    n[1] = n[0]
    n[0] = i
    x = use(n)
}
x += n[1] + n[0] + '</span>'
console.log(x)

function use1(a){
    let x = document.querySelector(`p:nth-child(${a})`)
    let n = ['', '', '']
    for (i of x.innerHTML){
        n[2] = n[1]
        n[1] = n[0]
        n[0] = i
        x.innerHTML = use2(n[2], n[1], n[0]) + n[1] + n[0]
    }
    console.log(x.innerHTML)
    x_ = ''
}
function use2(x1, x2, x3){
    x = x1 + x2 + x3
    if (x === ' is') {x_ += '</span>\n<span onclick="this_ = this; under()">'}
    if (x === ' so') {x_ += '</span>\n<span onclick="this_ = this; under()">'}
    if (x === 'tex') {x_ += '</span>\n<span onclick="this_ = this; under()">'}
    x_ += x1
    return x_
}
/*function use2(x1, x2, x3){
    x = x1 + x2 + x3
    if (x === 'tex') {x_ += '<span>'}
    x_ += x3
    return x_
}*/
function under(){
    let x = ''
    x = this_.style
    x.textDecoration !== 'underline'?
        x.textDecoration = 'underline'
    :
        x.textDecoration = 'none';
}
let x_ = ''

for (let i = 1; i < 1000; i++){
    
    if (document.querySelector(`p:nth-child(${i})`)){
    console.log(i);use1(i)
    }
}
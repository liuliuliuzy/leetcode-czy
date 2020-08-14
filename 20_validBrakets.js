/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    if(s.length == 0) return true
    var stack = new Array()
    var dict = {
        // 40: 41,
        // 91: 93,
        // 123: 125
        '{': '}',
        '[': ']',
        '(': ')'
    }
    for(let i=0; i<s.length; i++){
        // // console.log("1: ", stack, "2:", stack[stack.length-1], "3:", dict[s[i]])
        // if(stack[stack.length-1].charCodeAt() == 41 || stack[stack.length-1].charCodeAt() == 93 || stack[stack.length-1].charCodeAt() == 125){
        //     // stack.push(s[i])
        //     return false
        // } else if(dict[stack[stack.length-1].charCodeAt()] == s[i].charCodeAt()) {
        //     stack.pop()
        // } else {
        //     stack.push(s[i])
        // }
        if(stack[stack.length-1] == undefined){
            stack.push(s[i])
            continue
        }
        if(dict[stack[stack.length-1]] == undefined) return false
        else {
            if(dict[stack[stack.length-1]] == s[i]){
                stack.pop()
            } else {
                stack.push(s[i])
            }
        }
    }
    return stack.length == 0
};

var s = '[[()]]'
console.log(isValid(s))
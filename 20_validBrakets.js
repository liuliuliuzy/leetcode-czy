/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    if(s.length == 0) return true
    var stack = new Array()
    var dict = {
        '{': '}',
        '[': ']',
        '(': ')'
    }
    for(let i=0; i<s.length; i++){
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
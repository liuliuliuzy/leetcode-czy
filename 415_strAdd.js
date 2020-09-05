/**
 * @param {string} num1
 * @param {string} num2
 * @return {string}
 */
var addStrings = function(num1, num2) {
    function reverseStr(str){
        var res = ''
        var length = str.length
        for(let i=0; i<length; i++){
            res += str[length-1-i]
        }
        return res
    }
    var length1 = num1.length, length2 = num2.length
    var mLength = Math.max(length1, length2)
    var str1 = reverseStr(num1)
    var str2 = reverseStr(num2)
    var res = ''
    var carry = 0
    for(let i=0; i<mLength; i++){
        let a = i<length1?parseInt(str1[i]):0
        let b = i<length2?parseInt(str2[i]):0
        res += ((a+b+carry)%10).toString()
        carry = (a+b+carry)>9?1:0
    }
    if(carry > 0){
        res += '1'
    }
    return reverseStr(res)
};

var str1 = '1'
var str2 = '999'
console.log(addStrings(str1, str2))
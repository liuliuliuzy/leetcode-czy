/**
 * @param {string} s
 * @return {number}
 */
//js 的特殊性，s[i]在超出边界时是Undefined
var countBinarySubstrings = function(s) {
    var ans = 0
    var count=0, count_another=0
    var flag = true
    for(let i=0; i<s.length; i++){
        count_another+=1
        console.log(i<s.length && s[i+1] != s[i])
        if(i<s.length && s[i+1] != s[i]){
            console.log(count, count_another)
            ans += Math.min(count, count_another)
            count = count_another
            count_another = 0
        }
        // else{
        //     count += 1
        // }
    }
    console.log(count, count_another)
    return ans
};

var s = "00110"
console.log(countBinarySubstrings(s))
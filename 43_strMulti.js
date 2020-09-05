/**
 * @param {string} num1
 * @param {string} num2
 * @return {string}
 */
var multiply = function(num1, num2) {
    if(num1 == '0' || num2=='0'){
        return '0'
    }
    var length1 = num1.length, length2 = num2.length
    var res = new Array()
    for(let i=length1-1; i>-1; i--){
        let addCarry = 0
        let mulCarry = 0
        // let digitLists = new Array()
        for(let j=length2-1; j>-1; j--){
            let opIndex = length1+length2-2-(i+j)
            let num = res[opIndex]?res[opIndex]:0
            let mulRes = parseInt(num1[i])*parseInt(num2[j])+mulCarry
            mulCarry = parseInt(mulRes/10)
            // digitLists.push(res%10)
            let addRes = num+(mulRes%10)+addCarry
            res[opIndex] = addRes%10
            addCarry = parseInt(addRes/10)
        }
        if(addCarry || mulCarry){
            res[length2-1+length1-i] = addCarry+mulCarry
        }
    }
    var ans = ''
    for(let i=0; i<res.length; i++){
        ans = res[i].toString()+ans
    }
    return ans
};

var num1 = '123', num2 = '456'
console.log(multiply(num1, num2))
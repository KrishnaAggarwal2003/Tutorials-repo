// function to check if a number is even or not

// functions can help prevent redundancy

function even_checker(number){
    if (number%2==0){
        console.log(`${number} is even`)
        }else{
            console.log(`${number} is odd`)
    }
}

even_checker(52)

// function to give sum upto a nth number

function sum_for(number){
    let total = 0
    for (let i=0;i<=number;i++){
        total+=i
    }

    console.log(`Total upto ${number} using for is: ${total}`)
}

sum_for(100)

function sum_while(number){
    let sum = 0
    let i = 0
    while(i<=number){
        sum += i;
        i++
    }
    console.log(`Total upto ${number} using while is: ${sum}`)
}

sum_while(100)

// arrow functions --> part of modern JS
const arrowSum = (a,b) => {
    return a+b
}

console.log(arrowSum(3,4))

// for each method forEach(callback function)
// function defined in forEach method
// methods -- functions got associated with an object

let arr = [1,2,6,3,4,5]
arr.forEach(
    (val, idx) => {
        console.log(`${val} and index:- ${idx}`)
    }
)

// Here forEach is a higher order function; square is a callback function used in forEach
arr.forEach(
    function square(val){
        console.log(`Returning squared of val in arr:-\n ${val**2}`)
    }
)



// Map array method -- to create a new array
// filter method -- to select a few particulafr values

newArr = arr.map(
    (val) => {
        return val*2
    }
)

console.log(`New array:- ${newArr}`)

filter_arr = arr.filter(
    (val) => {
        return val%2==0
    }
)

console.log(`Filtered array:- ${filter_arr}`)

// Reduce method
const sum_output = arr.reduce(
    (prev,cur) => {
         return prev + cur
    }
)
console.log(`Sum of the arr:- ${sum_output}`)

const largest = arr.reduce(
    (prev,cur) => {
        return prev>cur ? prev : cur
    }
)

console.log(`Lagest num of arr:- ${largest}`)


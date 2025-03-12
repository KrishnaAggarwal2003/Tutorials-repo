// arrays == collection of items

// typeof an array is `object` key = index

// strings are immutable but arrays are mutable in JS

let marks = [70,82,92,95,87]; // array

console.log(
    `Marks: ${marks}\n
    Length: ${marks.length}`
)

for (let i=0;i<marks.length;i++){
    console.log(`Index:${i} and value:${marks[i]}`)
}

// Average of marks
let sum = 0
for (let val of marks){
    sum+=val
}
console.log(`Average marks: ${sum / marks.length}`)

let prices = [250,645,300,900,50]

console.log(`Before discount: ${prices}`)
for (let i in prices){
    prices[i] = 0.9 * prices[i]
}
console.log(`After discount: ${prices}`) // Arrays are mutable

// Array methods
console.log(`Push: ${marks.push(0.5) , marks}\n
Pop: ${marks.pop(), marks}\n
To string: ${str_marks = marks.toString(), typeof str_marks}\n
Concat: ${marks.concat(prices)}\n
Unshift: ${marks.unshift(0.05), marks}\n 
Shift: ${marks.shift(), marks}\n`)

let heroes = ["thor","iron-man","ant-man","spider-man"]

console.log(`Using slice: ${new_heros = heroes.slice(1,heroes.length), new_heros}\n
Using splice: ${heroes.splice(0,2,"black panther","dr strange"), heroes}`)


            
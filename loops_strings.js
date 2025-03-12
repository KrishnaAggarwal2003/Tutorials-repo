// for loops
// for (initialize ;stop cond. ;updation){execution part}

for (var i=0; i<=3; i++){
    console.log("Hello")
}
console.log("i value outside of for loop: ",i) // if used let in initialize, then i is restricted in the loop block

let sum = 0;
let last_num = 100;
for (let i=0;i<=last_num;i++){
    sum = sum+i;
}
console.log("Sum of first",last_num,"numbers: ",sum)


// while loops
let a = 0;
while (a<=5){
    console.log("a is: ",a)
    a++;
}

// do-while loop

let k = 0;
do{
    console.log("Hello sir");
    k++;
}while(k<=10);

// for-of loop :- strings,arrays
let val_name = "Tony Stark"
for (let val of val_name){
    console.log(val);
}

// for-in loop:- objects
const object = {
    Student: 'Adam Rose',
    University: 'Yale University',
    Major: 'CSE'
}

for (let key in object){
    console.log("Key: ",key, " Value is: ",object[key])
}

// Print even numbers from 0 to 100
// if-else condition in for loop
for (let first_num = 0; first_num<=last_num;first_num++){
    if (first_num%2 == 0){
        console.log(first_num, "is even")
    }else{console.log(first_num, "is odd")}
}

// Strings

let sample_str = "Peter Parker"
console.log("Length of string: ",sample_str.length)

for(let a = 0;a<sample_str.length;a++){
    console.log(sample_str[a]);
}

// template literals
// using backlashes(`) to have similar func, as (f'') in python. [String interpolation]

console.log(`length of the name ${sample_str} is: ${sample_str.length}\n Type is:\t${typeof sample_str}`)

/* \n - escape character
\t - tab space character */

// string methods
console.log(`String methods:-\n
    Upper case:\t${sample_str.toUpperCase()}\n
    Lower case:\t${sample_str.toLowerCase()}\n
    Trim:\t${sample_str.trim()}\n
    Sliced:\t${sample_str.slice(0 , 5)}\n
    Concat:\t${sample_str.concat(val_name)}\n
    replace:\t${val_name.replace("Tony" , "Howard")}\n
${val_name} starting with: ${val_name.charAt(0)}`)
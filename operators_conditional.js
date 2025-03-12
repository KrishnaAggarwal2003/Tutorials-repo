// syntax -> rules of a programming language

console.log("hello world");

// operators:-
/* Arithematic, modulus, exponential, increment,decrement */

let a = 10;
let b = 12;

console.log("a+b is: " + a+b); // + here will do the concatenation i.e resulting in string rather than a int. So, output is 1012
console.log("a+b is : ", a+b); // This will not concatenate, so resulting is a int i.e. 22

console.log("a exponent b: ",a**b);

// comaprison operator

let k = 5;
let q = "5";

console.log(" k===q: ", k===q); // compares data type of two variables, similarly there is !==

/* Logical:- 
AND - &&
OR - ||
NOT - !*/

let cond1 = a>b;
let cond2 = a===10;
console.log("cond1 and cond2: ", cond1 && cond2);
console.log("cond1 or cond2: ", cond1 || cond2);

// Conditional Statements

// If statement -- if (cond.){execute}
let age = 25;
if (age>=18){
    console.log("You can vote");
}else{
    console.log("You can't vote")
}

let mode = "dark";
let color;
if (mode == "dark"){
    color = "Black"
}else if (mode == "light"){
    color = "White"
}

console.log("color value: " + color)

// Whether a number is odd or even
// Using if-else statement:-
let number = 26;
if (number%2 == 0){
    console.log(number,"is even")
}else{
    console.log(number, "is odd")
}
// Using ternary operators:-
// condition ? "true output" : "false output"
let cost = 25;
let result = cost > 26 ? "expensive":"cheap";
console.log(result)


// MDN Web Docs for Documentation of web-developement tools

// switch statement in js -- see in MDN docs

let sample_num = prompt("Enter the number: ");
// prompt will take the input number in the web-page

let answer = sample_num % 5 == 0 ? "Multiple of 5" : "Not a multiple of 5";

console.log(sample_num, "is", answer)
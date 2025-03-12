// It is a dynamically typed language.
console.log("Hello World");

// Variables in JS
// Should use **camel case** for naming varibales.
age = 21;
fullName = "Jason Smith";

console.log('Name: ',fullName,'age:',age+1);
console.log('My name is',fullName,'and I am',age,'years old');

x = null;
y = undefined;
console.log('There are variables x and y in here which has',x,'and',y,'values');


// let,const,var:- 3 keywords to be used before variable name, as per need.
// If a variable is declared but not given a values, then it's undefined

let k;
console.log('k will give',k,'value')

let gradYear = 54; // declaring a variable
console.log(gradYear);

gradYear = 67; // updating a variable

console.log(gradYear);

// Data types :- 2-types == Primitive(7) and Non-primitive (e.g:- objects)
// Primitive(7):- Number, string, boolean, undefined, null, BigInt, symbol
// Although typeof variable equal to null comes as an object, it is still counted in Primitive.

// Object can be defined as collection of different variables
const student={
    fullName : "Satish Kumar", // key: value pair (same as in case of dictionary in python)
    age : 18,
    cpi : 8.8,
    isPass: true
};
console.log('Type of Student is:',typeof student)
console.log(
    'Name of student: ' + student.fullName,'\n',
    'Age is: ' + student.age,'\n',
    'Is he Pass: ' + student["isPass"],'\n'
);

// Values of keys inside the object can be updated.
student["cpi"] = 10;
console.log('Cpi changed to: '+ student.cpi)

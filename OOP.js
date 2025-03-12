// Object-Oriented programming in JS
// Classes & Objects

// example of an object
const student = {
    fullName: 'ABC',
    marks: 95,
    printMarks: function(){
        console.log(`Marks are ${this.marks}`); // this is the current object if wanna use the properties or method inside the object itself
        return ""
    },
    printInfo(){
        console.log(`Name is ${this.fullName} and he got ${this.marks} in the exam`)
        return ""
    }
}

console.log(student.printInfo())
console.log(student)

let arr = ["apple","banana","orange"]
console.log(arr.toString())
// By default properties or methods come through the Prototype (reference to an object) object which is automatically created in the user defined Object


const employee = {
    calcTax(money){
        console.log(`Tax to be paid on ${money} is = ${0.1*money}`)
        return ""
    }
}

const Salary = {
    sales: 50000
}

Salary.__proto__ = employee // I used prototype to define the object employee in the Prototype of Salary object. This way I am able to use calcTax function for the Salary

console.log(Salary.calcTax(Salary.sales))

// If same function is mentioned in object and prototype, then preference is given over object's method

// CLasses

class ToyotaCar{
    // constructor method
    constructor(purpose){
        console.log('creating new object')
        console.log(`${purpose} of this class`)
    }
    start(name){
        console.log(`Start function ${name}`)
        return ""
    };

    name(){
        return "Toyota model"
    };

    setBrand(brand){
        this.brandname = brand
    }

}

let models = new ToyotaCar('Defining car model')
console.log(models.start(models.name()))
console.log(models.setBrand('Suzuki'))
console.log(models.brandname) // Now, brandname has become a property for this class

let cars = new ToyotaCar('cars models') // Once the object was created with the class, constructor invoked automatically

cars.setBrand('Maruti')
console.log(cars.brandname)
cars.brandname = "Mclaren"
console.log(cars.brandname)

// constructor is similar to that __init__ function in classes python; One difference is that in constructor, we could also execute some tasks rather that just defining properties

// Inheritance in JS:- passing down properties & methods from parent class to child class

// f1 -- parent ,, f2 -- child

class f1{
    constructor(){
        console.log(`Enter parent constructor`)
    }
    start(){
        console.log(`Function of parent class`);
        return ""
    }
}

class f2 extends f1{
    constructor(relation){
        super(); // To invoke parent class constructor, necessary for derived (child) class constructor to execute
        console.log(`Enter the ${relation} constructor`)

    }
    
    stop(){
        console.log('Function of child class');
        return ""
    }
}

let baccha = new f2("first child")
console.log(baccha.start()) // start method inherited
console.log(baccha.stop())

// Error handling
let a = 5
let b = 10

// try-catch block for error handling
try{
    console.log(`Sum of a & b:- ${a+c}`)
}catch(err){
    console.log(`The error is ${err}`)
}
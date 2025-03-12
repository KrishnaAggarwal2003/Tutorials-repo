// Async await >> promise chains >> callback hell

// Synchronous programming:-  codes wold execute strictly via the line order they are written in the file

// Asynchronous:- the codes written after a particular code could be executed before that code. Not necessary to follow the order

// A simple example of Asynchronous code
console.log("one")
console.log("two")

setTimeout(() => {
    console.log("Three:- executing after 3 seconds")
}, 3000); // 3s -> 3000ms

console.log("four")
console.log("five")

// A simple example of callback (a function used as an arguement in another function)
function sum(a,b){
    return a+b
}

function calc(a,b,sumCallback){
    return sumCallback(a,b);
}

console.log(calc(1,2,sum)) // sum used as callback in calc function

// Callback hell:- Nesting of callbacks stacked one over other.

function getData(dataId, getNextdata){
    setTimeout(() => {
        console.log(` data ${dataId}`);
        getNextdata();
    }, 2000)
}

// an example of a nested callback
getData(1,()=>{
    getData(2,()=>{
        getData(3,()=>{console.log('Until 3 ids')});
    })
}) // Here get data 2 is callback for get data 1. So, first data 1 is executed then data 2 each taking 2 seconds

// callback hell:- Not a good way of programming

// Promises:- solution for callback hell
let promise = new Promise((resolve,reject)=>{
    console.log("I am a promise");
    resolve('Succeed')
    reject("Some error occurred")
})

console.log(promise)
// So basically, whenever for e.g:- a function for fetching data requests the data from the API, it will return a 'promise' object from which data is extracted

// then() & catch() methods in Promise. Then() only used when promise is fulfilled

const new_promise = ()=>{
    return new Promise((resolve,reject)=>{
        console.log("Data resolving");
        reject("failure")
        resolve("Success") // Here promise is already handled by rejection, so resolve line is ignored
    })
}

let promise_obj = new_promise()

setTimeout(()=>{promise_obj.then((res)=>{
    console.log(`Promise fulfilled:- ${res}`)
})},10000) // Will throw an error of unhandled rejection because promise is handled as a rejection rather than resolve

promise_obj.catch((err)=>{
    console.log(`Failed promise:- ${err}`) // When there is a rejection in the function of promise
})

function asyncwait1() {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            console.log("Data 1 fetched");
            resolve("Fetched successfully");
        }, 10000);
    });
}

function asyncwait2() {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            console.log("Data 2 fetched");
            resolve("Success");
        }, 15000);
    });
}


let p1 = asyncwait1()


p1.then((res)=>{
    console.log(`Data 1:- ${res}`);
    let p2 = asyncwait2();
    p2.then((res)=>{
    console.log(`Data 2:- ${res}`)
    })
}) // Example of promise chain

// Async-Await :- Better way for Promise chains
// Async func. always returns a promise

function api(){
    return new Promise((resolve,reject)=>{
        setTimeout(()=>{console.log(`Data 1 fetched`);
        resolve(200)}, 5000)
    })
}

function api2(){
    return new Promise((resolve,reject)=>{
        setTimeout(()=>{console.log(`Data 2 fetched`);
        resolve(200)}, 5000)
    })
}

(async function getWeatherdata(){
    console.log("Getting data 1")
    await api()
    console.log("Getting data 2")
    await api2()
})(); // Converted this into an IIFE function. This function would immediately execute by itself without even calling the func.name
      // Here, no need to call getWeatherdata(), it will automatically call on the await functions for data

// change in state of an object is called event
// They are fired to notify the changes (mostly done due to user-interface interaction) that may affect the code execution.
// e.g:- clicking of a button, keyboard keys etc.

let butt = document.querySelector("#first")
butt.ondblclick = (evt) => {
    console.log("It was clicked 2 times") // JS event handling
    console.log(evt) // event object
}

function summation(number){
    let sum = 0
    for (let i=0;i<=number;i++){
        sum+=i
    }
    return sum
}

const adder = (number) =>{
    let sum = 0
    for (let i=0;i<=number;i++){
        sum+=i
    }
    console.log(`Sum of ${number} numbers is ${sum}`)
}

function handleclick(){
    console.log(summation(100))
}

let summer = document.querySelector("#summ")

summer.addEventListener("click" , handleclick) // could handle multiple events

summer.removeEventListener("click", handleclick)

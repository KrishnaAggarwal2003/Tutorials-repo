// Fetching API's
// An interface for fetching resources

// let promise = fetch(url,[options]) // The code line for fetch, will return a promis object

const URL = "https://cat-fact.herokuapp.com/facts";


const api_button = document.querySelector("#api_call")
const facts = document.querySelector("#display")

const get_data = async () =>{
    console.log("Step 1:- Fetching data in JSON format")
    console.log("Getting data")
    let response = await fetch(URL)
    console.log(response) // In JSON format
    console.log(`Success:- ${response.status}`)

    console.log("Step 2:- Coverting JSON format data to JS object")
    let data = await response.json();
    console.log(data) // In a JS object format
    facts.innerText = data[2].text

} // With async-await

const get_data_with_chain = ()=>{
    fetch(URL)
    .then((response)=>{
        return response.json()
    })
    .then((data)=>{
        console.log(data);
        facts.innerText = data[0].text
    })
} // With promise chain

api_button.addEventListener("click", get_data_with_chain)

// Now, the aim is to convert the JSON format data into JS object
// json() method:- Input is JSON, output is JS object

// Document object model(DOM)(structured tree like str. with nodes(objects)) --> HTML code into form of objects.

// When a web-page is loaded, browser creates the DOM of the page

// HTML content is available in document object inside Window, which can be accessed in JS

// document --> object representation of HTML content
//console.log --> to print
// console.dir --> To print properties,methods in objects(e.g:- document)

// DOM cocnept can be used to dynamic bring changes according to user's preference in the web interface, rather than permanent changes in the HTML file code. 

// DOM manipulation functions:

let ids = document.getElementById("id_name") // To access the elements in the body by their ID name

let classes = document.getElementsByClassName("class_name") // accessing using class name, would get an HTML collection of tags sharing the same class name

let tags = document.getElementsByTagName("tag") // accessing tags

// To collectively select all the particular things from the HTML code, returns nodelist
document.querySelector("tags / class/ id") // 1st element
document.querySelectorAll("tags / class/ id") // all elements

// Properties
let sample = document.querySelector("tag/class/id")

sample.tagName
sample.innerHTML // could be used to update or change in HTML code of the sample object.
sample.innerText // could be used to change text within a tag
sample.textContent // could show text even for hidden elements.

sample.getAttribute // to get attributes assigned to this tag e.g:- name, id, class etc.
sample.style // tells about inline style given, if any

// insert or delete elements in tag

// DOM tree:- text,comment and element nodes
// parent, child, sibling nodes -- heirarchy of nodes in the tree.
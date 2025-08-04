let btn1 = document.querySelector("#addBtn");
let btn2 = document.querySelector("#clearAll");
let btn3 = document.querySelector("#DelTodo");
// btn1.onclick = () => {
//     console.log("Add button was clicked");
// }
// btn2.onclick = () => {
//     console.log("Clear All button was cliked");
// }
btn1.addEventListener("click", () => {
    console.log("Updating list..");
    let tit = document.getElementById("TodoTitle").value;
    let desc = document.getElementById("TodoDescription").value;
    let itemsJsonArray = [];
    if(localStorage.getItem('itemsJson')){
        itemsJsonArray.JSON.parse(localStorage.getItem('itemsJson'));
    }

    itemsJsonArray.push([tit,desc]);

    localStorage.setItem('itemJson',JSON.stringify(itemsJsonArray));

    console.log("Todo added:", [tit,desc]);
});

btn2.addEventListener("click", () => {
    console.log("Clearing list..");
    
})
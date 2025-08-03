add = document.getElementById("11");
add.addEventListener("Add"),()=>{
    console.log("updating list..");
    tit = document.getElementById("TodoTitle").value
    desc = document.getElementById("TodoDescription").value
    if (localStorage.getItem('itemsJson')) {
        itemJsonArray = [];
        itemJsonArray.push([tit,desc]);
        localStorage.setItem('itemJson',JSON.stringify(itemJsonArray))
    }
};
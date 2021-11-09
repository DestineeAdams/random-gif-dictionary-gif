
console.log("test");

async function getInfo() {
    const response = await fetch('values.json');
    const data = await response.json();

    document.getElementById("w").innerHTML = data.word;
    document.getElementById("d").innerHTML = data.definition;
    document.getElementById("i").src = data.gifLink;



} 

getInfo().catch(error => {
    console.log(error);
});




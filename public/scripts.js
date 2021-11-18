
console.log("test");

async function reload() {
    const response = await fetch('values.json');
    const data = await response.json();

    data.WasReloaded = true;

    getInfo().catch(error => {
        console.log(error);
    });

    window.location.reload();
    
}


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




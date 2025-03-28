function makeChanges() {
    document.querySelectorAll("img").forEach(image =>{
        image.src="timepass.png";
    });

    document.querySelector("h1").remove();
    document.querySelectorAll("p").forEach(para=>{
        para.innerText="Enough of JavaScript, lets stop.";
    });

    document.querySelectorAll("h2").forEach(para=>{
        para.innerText=para.innerText.toUpperCase();
    });
    
    first_div=document.getElementById("div1");
    first_div.innerHTML+="<h3></h3>";

}
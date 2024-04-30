
let darkmodeicon = document.querySelector('#darkmodeicon');
let root =  document.documentElement;


darkmodeicon.addEventListener('click',()=>{
    console.log('ddddddddddddddd');
    root.style.setProperty("--bgcolor", "#151515");
    root.style.setProperty("--primaryColor", "transparent");
    root.style.setProperty("--primaryFooter", "#252525");
    root.style.setProperty("--headerElementColor", "#fffff0");
    root.style.setProperty("--h3color", "#ccc");
    root.style.setProperty("--h1color", "#ddd");
    root.style.setProperty("--coursecode", "#999");
    root.style.setProperty("--creditcolor", "#00000000");
    root.style.setProperty("--placeholder", "#444");
    root.style.setProperty("--inputColor", "#999");
    root.style.setProperty("--topborder", "#e8787e");
    root.style.setProperty("--cgpacalc", "#252525");
    root.style.setProperty("--togglebg", "#666");
    root.style.setProperty("--upfeature", "#252525");
    root.style.setProperty("--upfeatureh3", "#fffff0");
    root.style.setProperty("--upfeatureshadow", "transparent");
    root.style.setProperty("--homeButtonBg", "#252525");
    root.style.setProperty("--homeButtonBorder", "transparent");
    document.getElementById("allHeader").style.backdropFilter = "blur(10px)";
})


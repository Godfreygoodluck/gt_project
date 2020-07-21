function AboutDropDown(){
    var dropdown = document.getElementById("about_Dropdown");

    if(about_Dropdown.style.display == 'none'){
        about_Dropdown.style.display = 'flex';
        about_Dropdown.style.flexDirection = 'column';
    }else{
        about_Dropdown.style.display = 'none';
    };


    window.onclick = function (event) {
        if (!event.target.matches('.dropbtn')) {
            about_Dropdown.style.display = 'none';
            
        }
    };
};
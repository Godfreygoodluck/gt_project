function GalleryDropDown(){
    var dropdown = document.getElementById("myDropdown");

    if(myDropdown.style.display == 'flex'){
        myDropdown.style.display = 'none';
    }else{
        myDropdown.style.display = 'flex';
        myDropdown.style.flexDirection = 'column';
    };


    window.onclick = function (event) {
        if (!event.target.matches('.dropbtn')) {
            myDropdown.style.display = 'none';
            
        }
    };
};
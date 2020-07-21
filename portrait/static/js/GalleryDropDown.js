function GalleryDropDown(){
    var dropdown = document.getElementById("myDropdown");

    if(myDropdown.style.display == 'none'){
        myDropdown.style.display = 'flex';
        myDropdown.style.flexDirection = 'column';
    }else{
        myDropdown.style.display = 'none';
    };


    window.onclick = function (event) {
        if (!event.target.matches('.dropbtn')) {
            myDropdown.style.display = 'none';
            
        }
    };
};
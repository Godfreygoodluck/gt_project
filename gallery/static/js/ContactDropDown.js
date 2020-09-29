function ContactDropDown(){
    var dropdown = document.getElementById("contact_Dropdown");

    if(contact_Dropdown.style.display == 'flex'){
        contact_Dropdown.style.display = 'none';
    }else{
        contact_Dropdown.style.display = 'flex';
        contact_Dropdown.style.flexDirection = 'column';
    };


    window.onclick = function (event) {
        if (!event.target.matches('.dropbtn')) {
            contact_Dropdown.style.display = 'none';
            
        }
    };
}; 


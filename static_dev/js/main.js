let menu_visible = false


function menu_clicked(){
    let desktop_menu = document.getElementById("desktop-menu-container")

    if(menu_visible){
        desktop_menu.style.display = "none"
        desktop_menu.style.flexDirection = "row"
        menu_visible = false
    }else{
        desktop_menu.style.display = "flex"
        desktop_menu.style.flexDirection = "column"
        menu_visible = true
    }
}
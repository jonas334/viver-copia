const $menu = document.getElementById('menu_toggle');
const $container = document.getElementById('container')
const $sidebar = document.getElementById('sidebar')

cambioTamañoDiv();

$width = document.documentElement.clientWidth;
window.addEventListener("resize", cambioTamañoDiv);

function cambioTamañoDiv(e){
    $width = document.documentElement.clientWidth;
    if ($container.classList.contains('open')) {
        let widthContainer = $width-320;
        $container.style.setProperty('--widthContainer', widthContainer+"px");
    } else if ($container.classList.contains('close')){
        $container.style.setProperty('--widthContainer', ($width-80)+"px");
    }
}

$menu.addEventListener('click', toggle);

function toggle(e) {
    if ($container.classList.contains('open')) {
        $container.classList.replace('open', 'close');
        $sidebar.classList.replace('open', 'close');
        cambioTamañoDiv();
    } else{
        $container.classList.replace('close', 'open');
        $sidebar.classList.replace('close', 'open');
        cambioTamañoDiv();
    }
}

const $usuarios = document.getElementById('usuarios');
const $submenu = document.getElementById('submenu');

$usuarios.addEventListener('click', usuariosToggle);

function usuariosToggle(e) {
    if ($submenu.classList.contains('open')) {
        $submenu.classList.replace('open', 'close');
        
    }else{
        $submenu.classList.replace('close', 'open');
    }
}


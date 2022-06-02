function agregar(){
    let select = document.getElementById("select").value;
    let select2 = document.getElementById("select2").value;
    let mensaje = document.getElementById("mensaje");

    valor = parseInt(select) + parseInt(select2)
    mensaje.innerHTML = "Precio: " + valor

    mensaje.innerHTML
}

function agregarLocalStorage(){
    let nombre = document.getElementById("nombre").value;

    localStorage.setItem("nombre", nombre)
}

function obtenerLocalStorage(){
    let mensaje = document.getElementById("mensaje");

    nombre = localStorage.getItem("nombre");

    mensaje.innerHTML = nombre
}